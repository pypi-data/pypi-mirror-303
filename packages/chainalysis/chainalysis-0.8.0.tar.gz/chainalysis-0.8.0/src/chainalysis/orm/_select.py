from abc import ABC, abstractmethod
from typing import Any, Union

import sqlalchemy
from sqlalchemy import (
    Column,
    ColumnCollection,
    ColumnExpressionArgument,
    Subquery,
    Table,
)
from typing_extensions import Self

from chainalysis._exceptions import ValueException
from chainalysis.sql._analytical import AnalyticalQuery
from chainalysis.sql._transactional import TransactionalQuery


class Select(sqlalchemy.Select, ABC):
    """
    Select is an abstract base class that represents an interface
    for an Object Relational Mapper (ORM) which queries a chain-specific
    table within Data Solutions.

    Select provides the structure for constructing and executing SQL queries
    using functions. Child classes must implement methods to retrieve
    tables and execute queries, which will return the appropriate result type.
    """

    def __init__(self, api_key: str, chain_table_name: str):
        """
        Construct a new Select.

        :param api_key: The API key for the Data Solutions API.
        :type api_key: str
        :param chain_table_name: The chain and table name formatted as 'chain.table'.
        :type chain_table_name: str
        :raises ValueException: If the table name is not formatted correctly.
        """
        chain_table_name_split = chain_table_name.split(".")
        if len(chain_table_name_split) != 2:
            raise ValueException(
                "Table must be formatted as 'chain.table'. Check your input."
            )
        self.api_key = api_key
        self._table = self._get_table(
            chain_table_name_split[0], chain_table_name_split[1]
        )
        super().__init__(self._table)

    @property
    def c(self) -> ColumnCollection:
        """
        Get the columns of the table.

        :return: A collection of column objects associated with the table.
        :rtype: ColumnCollection
        """
        return self.table.c

    @property
    def table(self) -> Table:
        """
        The chosen table to query.

        :return: A Table object.
        :rtype: Table
        """
        return self._table

    def sql(self) -> str:
        """
        Compile the query into a raw SQL string.

        :return: The compiled SQL query as a string.
        :rtype: str
        """
        return self.compile(compile_kwargs={"literal_binds": True}).string

    @abstractmethod
    def execute(self) -> Union[TransactionalQuery, AnalyticalQuery]:
        """
        Execute the query and create a Transactional or Analytical object.

        :return: Transactional or Analytical object.
        :rtype: Union[Transactional, Analytical]
        """
        raise NotImplementedError(
            "Execute method must be implemented by child classes."
        )

    def with_columns(self, *columns: Column) -> Self:
        """
        Select specific columns from the table for querying.

        Note: All columns are selected by default.
        Use this method to select specific columns.

        :param columns: The columns to be selected.
        :type columns: Column
        :return: A Select instance with the selected columns.
        :rtype: Select

        E.g.::

            select_query = query_1.with_columns(query_1.c.column1, query_1.c.column2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT "chain.table1".column1, "chain.table1".column2
            FROM "chain.table1"
        """
        return self.with_only_columns(*columns)

    # Overriding select methods

    def where(self, *whereclauses: ColumnExpressionArgument[bool]) -> Self:
        """
        Create a new Select with the given expression
        added to its WHERE clause, joined to the existing clause via AND, if any.

        :param whereclauses: The WHERE clauses to apply.
        :type whereclauses: ColumnExpressionArgument[bool]
        :return: A new Select with the WHERE clause applied.
        :rtype: Select

        E.g.::

            where_query = query_1.where(query_1.c.column1 == 1)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM "chain.table1"
            WHERE "chain.table1".column1 = 1
        """
        return super().where(*whereclauses)

    def select_from(self, table: Table) -> Self:
        """
        Return a new Select with the given FROM expression(s) merged into its list of FROM objects.

        :param table: The table to select from.
        :type table: Table
        :return: A new Select with the FROM clause applied.
        :rtype: Select

        E.g.::

            from chainalysis import func

            select_from_query = query_1.with_columns((func.count('*')).select_from(query_1.table))

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT COUNT(*) FROM "chain.table1"
        """
        return super().select_from(table)

    def limit(self, limit: int) -> Self:
        """
        Create a new Select with the given LIMIT clause applied.

        :param limit: The number of rows to limit the result set to.
        :type limit: int
        :return: A new Select with the LIMIT clause applied.
        :rtype: Select

        E.g.::

            limit_query = query_1.limit(10)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT * FROM "chain.table1"
            LIMIT 10
        """
        return super().limit(limit)

    def group_by(self, *columns: Column) -> Self:
        """
        Create a new Select with the given expression(s) added to its GROUP BY clause.

        :param columns: The columns to group by.
        :type columns: Column
        :return: A new Select with the GROUP BY clause applied.
        :rtype: Select

        E.g.::

            group_by_query = query_1.group_by(query_1.c.column1, query_1.c.column2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM "chain.table1"
            GROUP BY "chain.table1".column1, "chain.table1".column2
        """
        return super().group_by(*columns)

    def having(self, *having: ColumnExpressionArgument[bool]) -> Self:
        """
        Create a new Select with the given expression added to its HAVING clause
        joined to the existing clause via AND, if any.

        :param having: The HAVING clauses to apply.
        :type having: ColumnExpressionArgument[bool]
        :return: A new Select with the HAVING clause applied.
        :rtype: Select

        E.g.::

            having_query = query_1.group_by(query_1.c.column1).having(query_1.c.column1 == 1)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM "chain.table1"
            GROUP BY "chain.table1".column1
            HAVING "chain.table1".column1 = 1
        """
        return super().having(*having)

    def order_by(self, *clauses: Column) -> Self:
        """
        Create a new Select with the given list of ORDER BY criteria applied.

        :param clauses: The ORDER BY criteria to apply.
        :type clauses: Column
        :return: A new Select with the ORDER BY criteria applied.
        :rtype: Select

        E.g.::

            order_by_query = query_1.order_by(query_1.c.column1, query_1.c.column2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM "chain.table1"
            ORDER BY "chain.table1".column1, "chain.table1".column2

        """
        return super().order_by(*clauses)

    def join(
        self,
        target: Table,
        onclause: ColumnExpressionArgument = None,
        *,
        isouter: bool = False,
        full: bool = False,
    ) -> Self:
        """
        Create a SQL JOIN against this Select object's criterion
        and apply generatively, returning the newly resulting Select.

        :param target: The target table to join.
        :type target: Table
        :param onclause: The ON clause to apply. If omitted, an ON clause is generated automatically based on the ForeignKey linkages between the two tables, if one can be unambiguously determined, otherwise an error is raised.
        :type onclause: ColumnExpressionArgument, optional
        :param isouter: Whether to apply an outer join.
        :type isouter: bool, optional, default False
        :param full: Whether to apply a full join.
        :type full: bool, optional, default False
        :return: A new Select with the join operation applied.
        :rtype: Select
        :raises ValueError: If the ON clause is not provided and an unambiguous foreign key linkage cannot be determined.

        E.g.::

            join_query = query_1.join(query_2.table, query_1.c.column1 == query_2.c.column1)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT "chain.table1".column1, "chain.table1".column2, "chain.table1".column3
            FROM "chain.table1" JOIN "chain.table2"
            ON "chain.table1".column1 = "chain.table2".column1
        """
        return super().join(target, onclause=onclause, isouter=isouter, full=full)

    def outerjoin(
        self,
        target: Table,
        onclause: ColumnExpressionArgument,
        *,
        full: bool = False,
    ) -> Self:
        """
        Create a SQL LEFT OUTER JOIN against this Select object's criterion
        and apply generatively, returning the newly resulting Select.

        :param target: The target table to join.
        :type target: Table
        :param onclause: The ON clause to apply.
        :type onclause: ColumnExpressionArgument
        :param full: Whether to apply a full join.
        :type full: bool, optional, default False
        :return: A new Select with the outer join operation applied.
        :rtype: Select

        E.g.::

            outerjoin_query = query_1.outerjoin(query_2.table, query_1.c.column1 == query_2.c.column1)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT "chain.table1".column1, "chain.table1".column2, "chain.table1".column3
            FROM "chain.table1" LEFT OUTER JOIN "chain.table2"
            ON "chain.table1".column1 = "chain.table2".column1
        """
        return super().outerjoin(target, onclause, full=full)

    def outerjoin_from(
        self,
        from_: Column,
        target: Table,
        onclause: ColumnExpressionArgument,
        *,
        full: bool = False,
    ) -> Self:
        """
        Create a SQL LEFT OUTER JOIN against this Select object's criterion
        and apply generatively, returning the newly resulting Select.

        :param from_: The table to join from.
        :type from_: Table
        :param target: The target table to join.
        :type target: Table
        :param onclause: The ON clause to apply.
        :type onclause: ColumnExpressionArgument
        :param full: Whether to apply a full join.
        :type full: bool, optional, default False
        :return: A new Select with the outer join operation applied.
        :rtype: Select

        E.g.::

            outerjoin_from_query = query_1.outerjoin_from(query_1.table, query_2.table, query_1.c.column1 == query_2.c.column1)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM "chain.table1" LEFT OUTER JOIN "chain.table2"
            ON "chain.table1".column1 = "chain.table2".column1
        """
        return super().outerjoin_from(from_, target, onclause, full=full)

    def distinct(self) -> Self:
        """
        Create a new Select which will apply DISTINCT operation applied.

        :return: A new Select with the DISTINCT operation applied.
        :rtype: Select

        E.g.::

            distinct_query = query_1.distinct()

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT DISTINCT *
            FROM "chain.table1"
        """
        return super().distinct()

    def exists(self) -> Self:
        """
        Create a new subquery which will apply an EXISTS clause to the SELECT statement overall.

        :return: A new subquery with the EXISTS operation applied.
        :rtype: Select

        E.g.::

            query_1 = query_1.where(query_1.c.column1 == 1)
            exists_query = query_1.exists()

        The resulting SQL query will be:

        .. code-block:: sql

            EXISTS (SELECT * FROM "chain.table1" WHERE "chain.table1".column1 = 1)
        """
        return super().exists()

    def alias(self, name: str = None) -> Self:
        """
        Create a new Select object with the given name as an alias.

        :param name: The name of the alias.
        :type name: str, optional, default None
        :return: A new Select with the alias applied.
        :rtype: Select

        E.g.::

            alias_query = query_1.alias(name="alias")

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT "chain.table1".column1 AS column1
            FROM "chain.table1" AS alias
        """
        return super().alias(name)

    # Overriding compound select methods

    def union(self, *other: "Select") -> Self:
        """
        Create an SQL UNION alias of this Select against the
        given selectables provided as positional arguments.

        A union is the set of all rows returned by either the left or right
        selectables. If a row is present in both selectables, it will appear
        in the result set only once.

        :param other: One or more Selects with which to union.
        :type other: Select
        :return: A new Select with the union operation applied.
        :rtype: Select

        E.g.::

            union_query = query_1.union(query_2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT anon_1.column1
            FROM (SELECT "chain.table1".column1 AS column1
            FROM "chain.table1" UNION SELECT "chain.table1".column1 AS column1
            FROM "chain.table1" UNION SELECT "chain.table2".column1 AS column1
            FROM "chain.table2") AS anon_1
        """
        return self.with_columns(super().union(*other).alias())

    def union_all(self, *other: "Select") -> Self:
        """
        Create an SQL UNION ALL alias of this Select against
        the given selectables provided as positional arguments.

        :param other: One or more Selects with which to union all.
        :type other: Select
        :return: A new Select with the union all operation applied.
        :rtype: Select

        E.g.::

            union_all_query = query_1.union_all(query_2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT anon_1.column1
            FROM (SELECT "chain.table2".column1 AS column1
            FROM "chain.table2" UNION ALL SELECT "chain.table2".column1 AS column1
            FROM "chain.table2" UNION ALL SELECT "chain.table1".column1 AS column1
            FROM "chain.table1") AS anon_1
        """
        return self.with_columns(super().union_all(*other).alias())

    def except_(self, *other: "Select") -> Self:
        """
        Create an SQL EXCEPT alias of this Select against the
        given selectables provided as positional arguments.

        :param other: One or more Select with which to except.
        :type other: Select
        :return: A new Select with the except operation applied.
        :rtype: Select

        E.g.::

            except_query = query_1.except_(query_2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM (SELECT anon_1.column1 AS column1
            FROM (SELECT "chain.table".column1 AS column1
            FROM "chain.table" EXCEPT SELECT "chain.table".column1 AS column1
            FROM "chain.table" EXCEPT SELECT "chain.table".column2 AS column2
            FROM "chain.table") AS anon_1) AS anon_1
        """

        return self.with_columns(super().except_(*other).alias())

    def except_all(self, *other: "Select") -> Self:
        """
        Create an SQL EXCEPT ALL alias of this Select against the
        given selectables provided as positional arguments.

        :param other: One or more Selects with which to except all.
        :type other: Select
        :return: A new Select with the except all operation applied.
        :rtype: Select

        E.g.::

            except_all_query = query_1.except_all(query_2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM (SELECT "chain.name".column1 AS column1
            FROM "chain.name" EXCEPT ALL SELECT "chain.name".column2 AS column2
            FROM "chain.name") AS anon_1
        """
        return self.with_columns(super().except_all(*other).alias())

    def intersect(self, *other: "Select") -> Self:
        """
        Create an SQL INTERSECT alias of this Select against the
        given selectables provided as positional arguments.

        :param other: One or more Selects with which to intersect.
        :type other: Select
        :return: A new Select with the intersect operation applied.
        :rtype: Select

        E.g.::

            intersect_query = query_1.intersect(query_2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT anon_1.column1
            FROM (SELECT "chain.table".column1 AS column1
            FROM "chain.table" INTERSECT SELECT "chain.table".column1 AS column1
            FROM "chain.table" INTERSECT SELECT "chain.table2".column1 AS column1
            FROM "chain.table2") AS anon_1
        """
        return self.with_columns(super().intersect(*other).alias())

    def intersect_all(self, *other: "Select") -> Self:
        """
        Create an SQL INTERSECT ALL alias of this Select against
        the given selectables provided as positional arguments.

        :param other: One or more Selects with which to intersect all.
        :type other: Select
        :return: A new Select with the intersect all operation applied.
        :rtype: Select

        E.g.::

            intersect_all_query = query_1.intersect_all(query_2)

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT anon_1.column1
            FROM (SELECT "chain.table".column1 AS column1
            FROM "chain.table" INTERSECT ALL SELECT "chain.table".column1 AS column1
            FROM "chain.table" INTERSECT ALL SELECT "chain.table2".column1 AS column1
            FROM "chain.table2") AS anon_1
        """
        return self.with_columns(super().intersect_all(*other).alias())

    def lateral(self, name: str = None) -> Self:
        """
        Create an SQL LATERAL alias of this Select against
        the given selectables provided as positional arguments.

        :param name: The name of the lateral selection.
        :type name: str, optional, default None
        :return: A new Select with the lateral operation applied.
        :rtype: Select

        E.g.::

            lateral_query = query_1.where(query_1.c.column1 > 10).lateral(name="alias")

        The resulting SQL query will be:

        .. code-block:: sql

            SELECT *
            FROM LATERAL (
                SELECT *
                FROM "chain.table1"
                WHERE "chain.table1".column1 > 10
            ) AS alias
        """
        return self.with_columns(super().lateral(name).alias())

    @abstractmethod
    def _get_table(self, chain, table: str) -> Table:
        """
        Create a SQLAlchemy Table object for the given chain and table name.

        :param chain: The chain name.
        :param table: The table name.
        :return: A SQLAlchemy Table object.
        :rtype: Table
        :raises ValueException: If the chain or table does not exist in the database.
        """
        raise NotImplementedError(
            "_get_table method must be implemented by child classes."
        )


def union(*selects: Select) -> Subquery:
    """
    Create an SQL UNION of all the given Selects provided as
    positional arguments.

    :param selects: A list of Selects to union.
    :type selects: Select
    :return: A new Select with the union operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import union

        union_query = union(table1, table2)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT "chain.table1".column1 AS column1
        FROM "chain.table1" UNION SELECT "chain.table2".column1 AS column1
        FROM "chain.table2",
    """
    return sqlalchemy.union(*selects)


def union_all(*selects: Select) -> Subquery:
    """
    Create an UNION ALL of multiple Selects.

    :param selects: A list of Selects to union all.
    :type selects: Select
    :return: A new Select with the union all operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import union_all

        union_all_query = union_all(query_1, query_2)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT "chain.table1".column1 AS column1
        FROM "chain.table1" UNION ALL SELECT "chain.table2".column1 AS column1
        FROM "chain.table2",
    """
    return sqlalchemy.union_all(*selects)


def except_(*selects: Select) -> Subquery:
    """
    Create an SQL EXCEPT of all the given Selects provided as
    positional arguments.

    :param selects: A list of Selects to except.
    :type selects: Select
    :return: A new Select with the except operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import except_

        except_query = except_(query_1, query_2)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT "chain.table1".column1 AS column1
        FROM "chain.table1" EXCEPT SELECT "chain.table2".column1 AS column1
        FROM "chain.table2",
    """
    return sqlalchemy.except_(*selects)


def except_all(*selects: Select) -> Subquery:
    """
    Create an SQL EXCEPT ALL of all the given Selects provided as
    positional arguments.

    :param selects: A list of Selects to except all.
    :type selects: Select
    :return: A new Select with the except all operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import except_all

        except_all_query = except_all(query_1, query_2)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT "chain.table1".column1 AS column1
        FROM "chain.table1" EXCEPT ALL SELECT "chain.table2".column1 AS column1
        FROM "chain.table2",
    """
    return sqlalchemy.except_all(*selects)


def intersect(*selects: Select) -> Subquery:
    """
    Create an SQL INTERSECT of all the given Selects provided as
    positional arguments.

    :param selects: A list of Selects to intersect.
    :type selects: Select
    :return: A new Select with the intersect operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import intersect

        intersect_query = intersect(table1, table2)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT "chain.table1".column1 AS column1
        FROM "chain.table1" INTERSECT SELECT "chain.table2".column1 AS column1
        FROM "chain.table2",
    """
    return sqlalchemy.intersect(*selects)


def intersect_all(*selects: Select) -> Subquery:
    """
    Create an SQL INTERSECT ALL of all the given Selects provided as
    positional arguments.

    :param selects: A list of Selects to intersect all.
    :type selects: Select
    :return: A new Selects with the intersect all operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import intersect_all

        intersect_all_query = intersect_all(table1, table2)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT "chain.table1".column1 AS column1
        FROM "chain.table1" INTERSECT ALL SELECT "chain.table2".column1 AS column1
        FROM "chain.table2",
    """
    return sqlalchemy.intersect_all(*selects)


def lateral(select: Select, name: str = None) -> Subquery:
    """
    Create an SQL LATERAL of this Select

    :param select: A Select to lateral.
    :type select: Select
    :param name: The name of the lateral Select.
    :type name: str, optional, default None
    :return: A new Select with the lateral operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import lateral

        lateral_query = lateral(query_1.where(query_1.c.column1 > 10))

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT *
        FROM LATERAL (
            SELECT *
            FROM "chain.table1"
            WHERE "chain.table1".column1 > 10
        ) AS alias
    """
    return sqlalchemy.lateral(select, name)


def join(
    left: Table,
    right: Table,
    onclause: ColumnExpressionArgument = None,
    isouter=False,
    full=False,
) -> Subquery:
    """
    Create a new Select object, joining two tables.

    :param left: The left table to join.
    :type left: Table
    :param right: The right table to join.
    :type right: Table
    :param onclause: The ON clause to apply.
    :type onclause: ColumnExpressionArgument, optional
    :param isouter: Whether to apply an outer join.
    :type isouter: bool, optional, default False
    :param full: Whether to apply a full join.
    :type full: bool, optional, default False
    :return: A new Select with the join operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import join

        join_query = join(query_1.table, query_2.table_2, table1.c.column1 == table2.c.column1)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT *
        FROM "chain.table1"
        JOIN "chain.table2" ON "chain.table1".column1 = "chain.table2".column
    """
    return sqlalchemy.join(left, right, onclause=onclause, isouter=isouter, full=full)


def outerjoin(
    left: Table,
    right: Table,
    onclause: ColumnExpressionArgument = None,
    full: bool = False,
) -> Subquery:
    """
    Create a new Select object, joining two tables with a LEFT OUTER JOIN.

    :param left: The left table to join.
    :type left: Table
    :param right: The right table to join.
    :type right: Table
    :param onclause: The ON clause to apply.
    :type onclause: ColumnExpressionArgument, optional, default None
    :param full: Whether to apply a full join.
    :type full: bool, optional, default False
    :return: A new Select with the outer join operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import outerjoin

        outerjoin_query = outerjoin(
            left=query_1.table,
            right=query_2.table,
            onclause=query_1.c.column1 == query_2.c.column1
        )

    The resulting SQL query will be:

    .. code-block:: sql

            SELECT *
            FROM "chain.table1"
            LEFT OUTER JOIN "chain.table2"
            ON "chain.table1".column1 = "chain.table2".column1
    """
    return sqlalchemy.outerjoin(left, right, onclause=onclause, full=full)


def distinct(column: Column) -> Subquery:
    """
    Create an column-expression-level DISTINCT clause.

    :param column: The column to apply DISTINCT to.
    :type column: Column
    :return: A new Select with the DISTINCT operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import distinct

        distinct_query = distinct(query_1)

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT DISTINCT *
        FROM "chain.table1"
    """
    return sqlalchemy.distinct(column)


def exists(select: Select) -> Subquery:
    """
    Create an EXISTS clause.

    :return: A new Select with the EXISTS operation applied.
    :rtype: Subquery

    E.g.::

        from chainalysis.orm import exists

        stmt = query.with_columns().where(query.c.column1 == 1)
        exists_query = exists(stmt)

    The resulting SQL query will be:

    .. code-block:: sql

        EXISTS (SELECT * FROM "chain.table1" WHERE "chain.table1".column1 = 1)
    """
    return sqlalchemy.exists(select)


def and_(*clauses: ColumnExpressionArgument) -> ColumnExpressionArgument:
    """
    Create a conjunction of expressions joined by an AND.

    :param clauses: The expressions to join.
    :type clauses: ColumnExpressionArgument
    :return: A new conjunction of expressions.
    :rtype: ColumnExpressionArgument

    E.g.::

        from chainalysis.orm import and_

        and_query = query_1.where(
            and_(
                query_1.c.column1 == 1,
                query_1.c.column2 == 2
            )
        )

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT * FROM "chain.table1"
        WHERE "chain.table1".column1 = 1 AND "chain.table1".column2 = 2

    Python's & operator can also be used to create an AND clause::

        and_query = (query_1.c.column1 == 1) & (query_1.c.column2 == 2)
    """
    return sqlalchemy.and_(*clauses)


def or_(*clauses: ColumnExpressionArgument) -> ColumnExpressionArgument:
    """
    Create a conjunction of expressions joined by an OR.

    :param clauses: The expressions to join.
    :type clauses: ColumnExpressionArgument
    :return: A new conjunction of expressions.
    :rtype: ColumnExpressionArgument

    E.g.::

        from chainalysis.orm import or_

        or_query = query_1.where(
            or_(
                query_1.c.column1 == 1,
                query_1.c.column2 == 2
            )
        )

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT * FROM "chain.table1"
        WHERE "chain.table1".column1 = 1 OR "chain.table1".column2 = 2

    Python's | operator can also be used to create an OR clause::

        or_query = (query_1.c.column1 == 1) | (query_1.c.column2 == 2)
    """
    return sqlalchemy.or_(*clauses)


def not_(clause: ColumnExpressionArgument) -> ColumnExpressionArgument:
    """
    Create a negation of a clause.

    :param clause: The clause to negate.
    :type clause: ColumnExpressionArgument
    :return: A new negated clause.
    :rtype: ColumnExpressionArgument

    E.g.::

        from chainalysis.orm import not_

        not_query = query_1.where(not_(query_1.c.column1 == 1))

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT * FROM "chain.table1"
        WHERE NOT "chain.table1".column1 = 1

    Python's ~ operator can also be used to negate a clause::

        not_query = ~(query_1.c.column1 == 1)
    """
    return sqlalchemy.not_(clause)


def between(
    column: Column, lower_bound: Any, upper_bound: Any, symmetric: bool = False
) -> ColumnExpressionArgument:
    """
    Create a BETWEEN predicate clause.

    :param column: The column to apply the BETWEEN clause to.
    :type column: Column
    :param lower_bound: The lower bound of the BETWEEN clause.
    :type lower_bound: Any
    :param upper_bound: The upper bound of the BETWEEN clause.
    :type upper_bound: Any
    :param symmetric: Whether to apply a symmetric BETWEEN clause.
    :type symmetric: bool, optional, default False
    :return: A new BETWEEN clause.
    :rtype: ColumnExpressionArgument

    E.g.::

        from chainalysis.orm import between

        between_query = query_1.where(between(query_1.c.column1, 1, 10))

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT * FROM "chain.table1"
        WHERE "chain.table1".column1 BETWEEN 1 AND 10
    """
    return sqlalchemy.between(column, lower_bound, upper_bound, symmetric)


def case(
    *whens: Any,
    value: Any = None,
    else_: Any = None,
) -> ColumnExpressionArgument:
    """
    Create a CASE expression.

    :param whens: The WHEN clauses to apply.
    :type whens: Any
    :param value: The value to compare.
    :type value: Any, optional, default None
    :param else_: The ELSE clause to apply.
    :type else_: Any, optional, default None
    :return: A new CASE expression.
    :rtype: ColumnExpressionArgument

    E.g. using whens::

        from chainalysis.orm import case

        case_query = query_1.with_columns(
            case(
                (query_1.c.column1 == 1, "one"),
                (query_1.c.column2 == 2, "two"),
                else_="three"
            )
        )

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT
            CASE
                WHEN "chain.table1".column1 = 1 THEN 'one'
                WHEN "chain.table1".column2 = 2 THEN 'two'
                ELSE 'three'
            END

    E.g. using value::

        from chainalysis.orm import case

        case_query = query_1.with_columns(
            case(
                {
                    query_1.c.column1: "one",
                    query_1.c.column2: "two"
                },
                value=query_1.c.column1,
                else_="three"
            )
        )

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT
            CASE "chain.table1".column1
                WHEN "chain.table1".column1 THEN 'one'
                WHEN "chain.table1".column2 THEN 'two'
                ELSE 'three'
            END
    """
    return sqlalchemy.case(*whens, value=value, else_=else_)


def literal(value: Any) -> ColumnExpressionArgument:
    """
    Create a literal clause, bound to a bind parameter.

    :param value: The value to bind.
    :type value: Any
    :return: A new literal clause.
    :rtype: ColumnExpressionArgument

    E.g.::

        from chainalysis.orm import literal

        literal_query = query_1.with_columns(
            query_1.c.column1,
            literal(1).label("one")
        )

    The resulting SQL query will be:

    .. code-block:: sql

        SELECT "chain.table".column1, 1 AS one
        FROM "chain.table"
    """
    return sqlalchemy.literal(value)


func = sqlalchemy.func
