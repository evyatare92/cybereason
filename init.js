use admin;
db.auth("root","example");
use cr-db;
db.createCollection('users');
db.users.insert([{firstname: "dor", lastname: "shaul", username: "dordor1", password: "Pasfdqwhi2"},{firstname: "omri", lastname: "cohen", username: "omrico", password: "VhFjkd221"}, {firstname: "amattzia", lastname: "brandwein", username: "amatz", password: "amBrand2"},{firstname: "ben", lastname: "raz", username: "benraz9", password: "bmk93087fy73"},{firstname: "hadar", lastname: "kraus", username: "hkraus", password: "huGi3Fk39"}]);