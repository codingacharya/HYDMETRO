import streamlit as st

# Sample station list
stations = [
    "Miyapur", "JNTU College", "KPHB", "Kukatpally", "Ameerpet", "Punjagutta",
    "Irrum Manzil", "Khairatabad", "Lakdi-ka-pul", "Assembly", "Nampally",
    "MG Bus Station", "Sultan Bazaar", "Mettuguda", "Tarnaka", "Secunderabad East"
]

# Sample fare matrix (simplified, flat rate logic)
base_fare = 10
fare_per_station = 5

# Title
st.title("Hyderabad Metro Ticket Booking")

# User inputs
from_station = st.selectbox("From Station", stations)
to_station = st.selectbox("To Station", stations)
ticket_type = st.radio("Ticket Type", ["Single", "Return"])
num_passengers = st.number_input("Number of Passengers", min_value=1, step=1)

# Validate station selection
if from_station != to_station:
    # Calculate fare
    distance = abs(stations.index(to_station) - stations.index(from_station))
    fare = base_fare + (distance * fare_per_station)
    if ticket_type == "Return":
        fare *= 2
    total_fare = fare * num_passengers

    # Book button
    if st.button("Book Ticket"):
        st.success("✅ Ticket Booked Successfully!")
        st.markdown("---")
        st.subheader("🎟️ Ticket Summary")
        st.write(f"**From:** {from_station}")
        st.write(f"**To:** {to_station}")
        st.write(f"**Type:** {ticket_type}")
        st.write(f"**Passengers:** {num_passengers}")
        st.write(f"**Fare per Ticket:** ₹{fare}")
        st.write(f"**Total Fare:** ₹{total_fare}")
else:
    st.warning("Please select different stations for From and To.")

