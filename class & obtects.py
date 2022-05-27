class Student:
    # [assignment] Skeleton class. Add your code here
   
    def __init__(self, name: str, age: int, track: list, score: float):
        self.name= name
        self.age= age
        self.tracks= tracks
        self.score= score
    def __str__(self):
    	 return f"Name: {self.name}, Age: {self.age}, Tracks: {self.tracks[0]} {self.tracks[1]} {self.tracks[2]}"
    	 
    
    def change_name(self, name: str):
      	self.name = name
      	print("Name: ", self.name)
      	return self.name

    def change_age(self, age: int):
      	self.age = age
      	print("Age: ", self.age)
      	return self.age
     
    def add_track(self, tracks: list):
           self.tracks.append(track)
           print("Tracks: ", self.tracks)
           return self.tracks
           
    def get_score(self):
           print("Score: ", self.score)
           return self.score
           
           
 
Bob = Student(name: "Bob", age: 26, tracks: ["FE","BE "], score: 20.90)

# Expected methods

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
print(Bob)