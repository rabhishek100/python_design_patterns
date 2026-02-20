from People import Driver, Rider
from Vehicles import Bike, Car, SmallCar, LargeCar, LuxCar
from Rides import Ride
from Pricing import NormalCost, SurgeCost, LuxCost, SharingCost
from Matcher import Matcher


if __name__ == "__main__":

    drivers = [

        Driver(
            name="abc",
            phone="1231232",
            rating=4,
            location="10 10",
            vehicle=Car(
                name="camry",
                number="tn45dfsdf"
            ),
        ),

        Driver(
            name="def",
            phone="6456364",
            rating=5,
            location="1 10",
            vehicle=LuxCar(
                name="Rolls Royce",
                number="gfgdgsdsg"
            ),
        ),

        Driver(
            name="xyz",
            phone="5453646",
            rating=3,
            location="10 1",
            vehicle=Car(
                name="camry",
                number="sgsgsv4f"
            ),
        ),

        Driver(
            name="qwe",
            phone="96677567",
            rating=5,
            location="1 1",
            vehicle=Bike(
                name="Splendor",
                number="gfgftttt"
            ),
        )

    ]

    ride_requests = [

        Ride(
            from_place="1 3",
            to="12 7",
            ride_duration="10 mins",
            request_time="10 pm",
            pricing=NormalCost(),
            rider=Rider(
                name="cxvxcvv",
                phone="54677777",
                rating=5,
                location="1 3",
            ),
        ),

        Ride(
            from_place="10 3",
            to="12 3",
            ride_duration="10 mins",
            request_time="10 pm",
            pricing=SurgeCost(),
            rider=Rider(
                name="dbbmfvv",
                phone="987654",
                rating=5,
                location="10 3",
            ),
        ),

        Ride(
            from_place="10 10",
            to="4 3",
            ride_duration="10 mins",
            request_time="10 pm",
            pricing=LuxCost(),
            rider=Rider(
                name="bgskzxczc",
                phone="5797654",
                rating=5,
                location="10 10",
            ),
        ),

        Ride(
            from_place="8 2",
            to="12 15",
            ride_duration="10 mins",
            request_time="10 pm",
            pricing=SharingCost(num_share=2),
            rider=Rider(
                name="bnshjdfh",
                phone="64746488",
                rating=5,
                location="8 2",
            )
        )

    ]


    matcher = Matcher()


    for driver in drivers:
        matcher.add_driver(driver)

    for ride in ride_requests:
        matcher.add_ride_request(ride)


    matched_rides = matcher.make_matches()

    print("Matched rides:")
    for ride, driver in matched_rides:
        print(f"  {ride.rider.name} matched with {driver.name}")

    print("\nStatus updates:")
    for ride, _ in matched_rides:
        ride.start_ride()
        ride.print_status()
        ride.complete_ride()
        ride.print_status()

    print("\nNotification history:")
    for ride, driver in matched_rides:
        ride.rider.print_notifications()
        driver.print_notifications()

    print("\nFare calculation:")
    for ride, _ in matched_rides:
        ride.print_fare()

    print("\nRe-match after completion (drivers should be available again):")
    follow_up_ride = Ride(
        from_place="2 2",
        to="4 4",
        ride_duration="5 mins",
        request_time="10:30 pm",
        pricing=NormalCost(),
        rider=Rider(
            name="new_rider",
            phone="100200300",
            rating=5,
            location="2 2",
        ),
    )
    matcher.add_ride_request(follow_up_ride)
    second_matches = matcher.make_matches()
    for ride, driver in second_matches:
        print(f"  {ride.rider.name} matched with {driver.name}")
