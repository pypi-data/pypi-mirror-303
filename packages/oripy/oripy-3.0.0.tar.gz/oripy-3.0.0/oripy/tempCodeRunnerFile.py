    def list(self):
        
        print(self.cdt.input)
        
        def list_all_functions(self):
        function_names = [
            "naivebayes",
            "id3",
            "fptree",
            "pagerank",
            "kmeans",
            "apriori",
            "olap",
            "input"
        ]

        print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        for name in function_names:
            print(f"{name.capitalize()} Function:")
            # Call the respective method based on the name
            getattr(self, name)()
            print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")


