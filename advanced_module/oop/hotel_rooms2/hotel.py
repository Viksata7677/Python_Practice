from hotel_rooms2.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if room.take_room(people):
                    self.guests += people
                break

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                if room.free_room():
                    self.guests -= room.guests
                break


    def status(self):
        free_rooms_num = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms_num = [str(room.number) for room in self.rooms if  room.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {", ".join(free_rooms_num)}\n"
                f"Taken rooms: {", ".join(taken_rooms_num)}")

hotel = Hotel.from_stars(5)


first_room = Room(1, 3)

second_room = Room(2, 2)

third_room = Room(3, 1)


hotel.add_room(first_room)

hotel.add_room(second_room)

hotel.add_room(third_room)


hotel.take_room(1, 4)

hotel.take_room(1, 2)

hotel.take_room(3, 1)

hotel.take_room(3, 1)


print(hotel.status())