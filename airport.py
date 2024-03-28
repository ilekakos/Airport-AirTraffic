"""
Eισαγωγή της βιβλιοθήκης queue για τη δημιουργία ουρών,
random για τη δημιουργία τυχαίων αριθμών,
time για τη διαχείριση του χρόνου
"""
import queue
import random
import time

## Ορισμός της κλάσης Flight για την αναπαράσταση των πτήσεων και των ενεργειών τους 
class Flight:
    def __init__(self, flight_number, action): # Ορίζουμε τον κατασκευαστή της κλάσης 
        self.flight_number = flight_number # Ο αριθμός της πτήσης
        self.action = action # Η ενέργεια που ζητείται (προσγείωση, απογείωση, εκτάκτου ανάγκης κλπ.)

    def __lt__(self, other): # Ορίζουμε τη σύγκριση μεταξύ δύο πτήσεων
        priorities = {"emergency": 0, "landing": 1, "takeoff": 2} # Ορίζουμε τις προτεραιότητες των ενεργειών
        return priorities[self.action] < priorities[other.action] # Επιστρέφουμε το αποτέλεσμα της σύγκρισης

# Ορισμός της συνάρτησης handle_requests για την εξυπηρέτηση των αιτημάτων πτήσεων
def handle_requests(landing_queue, takeoff_queue, emergency_queue): # Ορίζουμε τη συνάρτηση με τρεις ουρές
    while not emergency_queue.empty(): 
        flight = emergency_queue.get()
        print(f"CONTROL: {flight.flight_number} land (emergency)") 

    while not landing_queue.empty(): # Όσο η ουρά προσγείωσης δεν είναι άδεια
        flight = landing_queue.get()
        print(f"CONTROL: {flight.flight_number} land")

    while not takeoff_queue.empty():
        flight = takeoff_queue.get()
        print(f"CONTROL: {flight.flight_number} takeoff")

# Δημιουργία των ουρών προτεραιοτήτων για προσγειώσεις, απογειώσεις και εκτάκτες ανάγκες
landing_queue = queue.PriorityQueue()
takeoff_queue = queue.PriorityQueue()
emergency_queue = queue.PriorityQueue()


# Αρχικοποίηση του βρόχου επανάληψης για την προσομοίωση των αιτημάτων πτήσεων
while True:
    num_requests = random.randint(1, 3) # Τυχαίος αριθμός αιτημάτων πτήσεων
    for _ in range(num_requests):
        action = random.choices(["landing", "takeoff", "emergency"], weights=[4, 4, 1])[0] # Τυχαία επιλογή ενέργειας 
        flight_number = random.randint(100, 999) 
        flight = Flight(flight_number, action) # Δημιουργία της πτήσης
        
        # Εισαγωγή της πτήσης στην κατάλληλη ουρά
        if action == "emergency": 
            emergency_queue.put(flight)
        elif action == "landing":
            landing_queue.put(flight)
        else:
            takeoff_queue.put(flight)

        print(f"Flight {flight_number} requests {action}")
        
    

    # Εξυπηρέτηση των αιτημάτων πτήσεων
    handle_requests(landing_queue, takeoff_queue, emergency_queue) 
    time.sleep(1.5) # Αναμονή 1.5 δευτερολέπτων

