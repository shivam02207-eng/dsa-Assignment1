 # Weather Record ADT
class WeatherRecord:
    def _init_(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature


# Data Storage Class
class WeatherDataStorage:
    def _init_(self, years, cities):
        # create a 2D array [years][cities] 
        self.data = [[None for _ in range(len(cities))] for _ in range(len(years))]
        self.years = years
        self.cities = cities

    def populate_array(self, records):
        """Fill the 2D array with given records"""
        for rec in records:
            # extract year from date
            year = int(rec.date.split("/")[-1])
            if year in self.years and rec.city in self.cities:
                r = self.years.index(year)
                c = self.cities.index(rec.city)
                self.data[r][c] = rec.temperature

    def row_major_access(self):
        """Access data row by row"""
        values = []
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                values.append(self.data[r][c])
        return values

    def column_major_access(self):
        """Access data column by column"""
        values = []
        for c in range(len(self.cities)):
            for r in range(len(self.data)):
                values.append(self.data[r][c])
        return values

    def handle_sparse_data(self, sentinel=-9999):
        """Replace None with sentinel value for missing data"""
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c] is None:
                    self.data[r][c] = sentinel

    def analyze_complexity(self):
        # Insert -> O(1) if indices are known
        # Retrieve -> O(1)
        # Delete -> O(1) (just replace with sentinel)
        # Space -> O(n*m)
        return {
            "insert": "O(1)",
            "delete": "O(1)",
            "retrieve": "O(1)",
            "space": f"O({len(self.data)}*{len(self.cities)})"
        }


# ---------------------- TESTING -----------------------
if _name_ == "_main_":
    years = [2023, 2024]
    cities = ["Delhi", "Mumbai", "Chennai"]

    system = WeatherDataStorage(years, cities)

    records = [
        WeatherRecord("01/01/2023", "Delhi", 15.5),
        WeatherRecord("05/02/2023", "Mumbai", 28.1),
        WeatherRecord("10/03/2024", "Chennai", 31.0),
    ]

    system.populate_array(records)

    print("Row-major traversal:", system.row_major_access())
    print("Column-major traversal:", system.column_major_access())

    system.handle_sparse_data()
    print("Data after handling sparse values:", system.data)

    print("Complexity analysis:", system.analyze_complexity())
