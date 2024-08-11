import time
import pygame
import pyttsx3
import tkinter as tk
import threading


class Flight:
    def __init__(self, flight_number, destination, departure_time, gate, status):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.gate = gate
        self.status = status

    def __str__(self):
        return (
            f" Flight {self.flight_number} to {self.destination}"
            f" Departuring at {self.departure_time} from gate {self.gate}."
            f" Status:{self.status} "
        )


class AirportAnnouncementSystem:
    def __init__(self):
        self.flights = []
        pygame.mixer.init()
        self.engine = pyttsx3.init()

        self.root = tk.Tk()
        self.root.title("Airport Flight Announcement System")
        self.text_widget = tk.Text(self.root, height=15, width=50)
        self.text_widget.pack()

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f" Added : {flight}")

    def play_announcement_sound(self):
        pygame.mixer.music.load(
            "Flight Deparure & Arrival Announcement System/May I have your attention please! sound effect  No Copyright  Free Download.mp3"
        )
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def announce_flights(self):
        while True:
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, "\nCurrent Flight Announcements :\n")
            for flight in self.flights:
                announcement = str(flight)
                print(announcement)
                self.text_widget.insert(tk.END, announcement + "\n")
                self.play_announcement_sound()
                self.engine.say(announcement)
                self.engine.runAndWait()
                self.root.update()
                time.sleep(10)


announcement_system = AirportAnnouncementSystem()

announcement_system.add_flight(
    Flight("AA102", "Washington DC", "22:30", "A13", "On Time")
)
announcement_system.add_flight(Flight("AB102", "Singapore", "15:00", "B15", "Delayed"))
announcement_system.add_flight(Flight("CA108", "Edinburg", "16:30", "D08", "On Time"))
announcement_system.add_flight(Flight("AA102", "New Dellhi", "14:00", "B14", "Delayed"))
announcement_system.add_flight(Flight("AA102", "Agartala", "13:00", "C118", "Delayed"))


import threading

threading.Thread(target=announcement_system.announce_flights).start()


announcement_system.root.mainloop()
