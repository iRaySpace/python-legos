import pandas as pd


def main():
    users = pd.read_csv("datasets/users.csv")

    # Exercise #1: Basic SELECT, WHERE, ORDER BY

    # New column
    one_users = users.copy()
    one_users["salary_k"] = one_users["salary"] / 1000

    # WHERE and SELECT and ORDER BY
    filtered_users = one_users[
        (one_users["country"] == "PH") & (one_users["salary"] >= 40_000)
    ][["name", "country", "salary", "salary_k"]].sort_values("salary", ascending=False)
    print(filtered_users)

    # Exercise #2: GROUP BY, AGGREGATES, HAVING
    two_users = users.copy()

    two_users = (
        two_users.groupby("country")
        .agg(
            total_users=("id", "count"),
            avg_salary=("salary", "mean"),
            max_salary=("salary", "max"),
        )
        .query("avg_salary >= 50_000")
        .sort_values("avg_salary", ascending=False)
        .reset_index()
    )
    print(two_users)

    # Exercise #3: JOIN, GROUP BY, FILTERING
    orders = pd.read_csv('datasets/orders.csv')
    print(orders)

    users_and_orders = (
        pd.merge(users, orders, how='left', left_on='id', right_on='user_id')
        .groupby('id')
        .agg(
            name=('name', 'first'),
            total_orders=('order_id', 'count'),
            total_spent=('amount', 'sum'),
        )
        .query('total_spent >= 500')
        .sort_values('total_spent', ascending=False)
        .reset_index()
    )
    print(users_and_orders)

if __name__ == "__main__":
    main()
