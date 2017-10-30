print("Start init");

conn = new Mongo();

db = conn.getDB("admin");
db.createUser(
  {
    user: "admin",
    pwd: "admin",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
);

db.auth("admin", "admin");

db = conn.getDB("pitchme");

db.createUser(
  {
    user: "admin",
    pwd: "admin",
    roles: [ { role: "userAdmin", db: "pitchme" } ]
  }
);

db.auth("admin", "admin");

db.createUser(
  {
    user: "writer",
    pwd: "writer",
    roles: [ { role: "readWrite", db: "pitchme" } ]
  }
);

db.auth("writer", "writer");

db.createCollection("users");
db.createCollection("positions");
db.createCollection("requests");

print("End script");