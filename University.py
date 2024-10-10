universities = [
    {
        "university_name": "University of Demacia", 
        "location": "123 Academy Lane, Demacia City, Valoran, 45678", 
        "established": "2009", 
        "number_of_students": 15000, 
        "university_type": "Private"
    },
    {
        "university_name": "University of Noxus", 
        "location": "456 Conqueror's Way, Noxus City, Runeterra, 12345", 
        "established": "2005", 
        "number_of_students": 18000, 
        "university_type": "Private"
    },
    {
        "university_name": "University of Ionia", 
        "location": "789 Harmony Path, Ionia Village, Runeterra, 67890", 
        "established": "2007", 
        "number_of_students": 12000, 
        "university_type": "Public"
    },
    {
        "university_name": "University of Targon", 
        "location": "321 Celestial Way, Targon Peaks, Runeterra, 13579", 
        "established": "2002", 
        "number_of_students": 21000, 
        "university_type": "Private"
    },
    {
        "university_name": "University of Shurima", 
        "location": "987 Sun Disk Road, Shurima Desert, Runeterra, 24680", 
        "established": "2002", 
        "number_of_students": 9500, 
        "university_type": "Private"
    }
]

for university in universities:
    print(f"University Name: {university['university_name']} | Location: {university['location']} | Established: {university['established']} | Number of Students: {university['number_of_students']} | University Type: {university['university_type']}")
