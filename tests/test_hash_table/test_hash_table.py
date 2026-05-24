from src.hash_table.hash_table import Node, HashTable

def test_put():
    hash_table: HashTable = HashTable()
    hash_table.put("name", "Asmaa")
    hash_table.put("age", 25)
    hash_table.put("university", "Birzeit")

    assert hash_table.size == 3

def test_get():
    hash_table: HashTable = HashTable()
    hash_table.put("name", "Asmaa")
    hash_table.put("age", 25)
    hash_table.put("university", "Birzeit")
    
    
    assert hash_table.get("age") == 25
    assert hash_table.get("name") == "Asmaa"
    assert hash_table.get("weight") == "key not found"

def test_remove():
    hash_table: HashTable = HashTable()
    hash_table.put("name", "Asmaa")
    hash_table.put("age", 25)
    hash_table.put("university", "Birzeit")
    assert hash_table.get("age") == 25
    assert hash_table.size == 3
    hash_table.remove("name")
    assert hash_table.get("name") == "key not found"
    assert hash_table.size == 2

def test_search():
    hash_table: HashTable = HashTable()
    hash_table.put("name", "Asmaa")
    hash_table.put("age", 25)
    hash_table.put("university", "Birzeit")
    assert hash_table.search("weight") is False
    assert hash_table.search("name") is True


