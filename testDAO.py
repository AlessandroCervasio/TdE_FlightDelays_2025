from database.DAO import DAO

dao=DAO()
lista= dao.getAllEdges()
print (len(lista))