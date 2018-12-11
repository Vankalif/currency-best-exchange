def read_sql(path: str) -> str:
    with open(path) as file:
        qry = file.read()
        return qry
