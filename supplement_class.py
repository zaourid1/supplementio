"""
-------------------------------------------------------
Supplement class definition.
-------------------------------------------------------
Author:  Zineb Aourid
__updated__ = "2025-08-03"
-------------------------------------------------------
"""

class Supplement:
    """
    Defines data for a single supplement: id, name, symptoms, recommendation.
    """
    # Constants

    #@staticmethod
    def __init__(self, id, name, symptoms, recs):
        """
        -------------------------------------------------------
        Initializes a Supplement object.
        Use: supplement = Supplement(id, name, symptoms, recommendation)
        -------------------------------------------------------
        Parameters:
            id - unique id (int)
            name - supplement name (str)
            symptoms - list of symptoms (str list)
            recommendation - doses recommeneded (str)
        Returns:
            A new Supplement object (Supplement)
        -------------------------------------------------------
        """
    
        assert id >= 0, "Id must be a postive int "
        
        self.id = id
        self.name = name
        self.symptoms = symptoms if symptoms is not None else "Unknown"
        self.recs = recs

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of supplement data.
        Use: print(supplement)
        Use: print( "{}".format(supplement))
        Use: string = str(supplement)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of supplemtn (str)
        -------------------------------------------------------
        """
        string = """ID:    {}
            Name:     {}
            Symptoms: {}
            Recs:   {}""".format(self.id, self.name, self.symptoms, self.recs)
        return string

    def __eq__(self, other):
        """
        -------------------------------------------------------
        Compares this supplement against another supplement for equality.
        Use: movie == other
        -------------------------------------------------------
        Parameters:
            other - other movie to compare to (Supplement)
        Returns:
            result - True if id and name match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.id, self.name.lower()) == \
            (other.id, other.name.lower())
        return result
    
    def __repr__(self):
        '''
        Printing the ID and Name only.
        '''
        return f"Supplement({self.id}, {self.name})"

s = Supplement(1, "Vitamin D3", ["fatigue", "bone pain", "low sun exposure", "frequent colds"], "2000 IU Vitamin D3 daily")

print(s)