from src.hash_table.hash_table import Node, HashTable
def test_put():
    hash_table: HashTable = HashTable()
    hash_table.put("name", "Asmaa")
    hash_table.put("age", 25)
    hash_table.put("university", "Birzeit")

    assert hash_table.size == 3

