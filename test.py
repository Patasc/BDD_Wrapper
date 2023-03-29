import Model
import ConnectionHandler
import Utils.Dotenv as Dotenv
from CacheDatabase import CacheDatabase

Db = ConnectionHandler.initiate(Dotenv.getenv("DB_TYPE"))
CacheDb = CacheDatabase(Db, Model.tables)
QueryBuilder = Model.Model(CacheDb)

# QueryBuilder.table("Users", "insert").where("firstname", "1").where("lastname", "2").where("password", "a").execute()

# res = QueryBuilder.table("Users").execute()
# print(res)

# print(QueryBuilder.table("Users").where("id", "3").execute())
# print(QueryBuilder.table("Users").select("id", "firstname").execute())


print(QueryBuilder.table("Users").select("id", "firstname").execute())
print(QueryBuilder.table("Users", "insert").where("firstname", "1").where("lastname", "2").where("password", "a").execute())
print(QueryBuilder.table("Users").select("id", "firstname").execute())
print(QueryBuilder.table("Users", "delete").where("id", "d2a6fcc8-06b7-4c95-8207-c817c02199a0").execute())
print(QueryBuilder.table("Users").select("id", "firstname").execute())
print(QueryBuilder.table("Users", "alter", "ca78b376-4383-48c1-bb16-0327b2259108").where("firstname", "Prénom").execute())
print(QueryBuilder.table("Users").select("id", "firstname").execute())



id_seq = QueryBuilder.table("Sequences", "insert").where("label", "Ceci est un label").execute()
id_ques = QueryBuilder.table("Questions", "insert").where("label", "label").where("slug", "slug").where("enonce", "enonce ici").where("type", "libre").where("user_id", "ca78b376-4383-48c1-bb16-0327b2259108").execute()

print(QueryBuilder.table("question_sequence", "insert").where("sequence_id", id_seq).where("question_id", id_ques).execute())
