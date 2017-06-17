from ghh_input_error import GHHInputError

class Team:
    """A Game of Hip-Hop (GHH) team"""
    def __init__(self):
        self.PRODUCER_LIMIT = 2
        self.RAPPER_LIMIT = 3
        self.producers = []
        self.rappers = []
  
    def add_rappers(self, rappers):
        for rapper in rappers:
            self.add_rapper(rapper)

    def add_producers(self, producers):
        for producer in producers:
            self.add_producer(producer)
    
    def add_rapper(self, rapper):
        if len(self.rappers) < self.RAPPER_LIMIT:
            self.rappers.append(rapper)
        else:
            raise GHHInputError("Rapper limit of %d reached when adding '%s'" % (self.RAPPER_LIMIT, rapper))
      
    def add_producer(self, producer):
        if len(self.producers) < self.PRODUCER_LIMIT:
            self.producers.append(producer)
        else:
            raise GHHInputError("Producer limit of %d reached when adding '%s'" % (self.PRODUCER_LIMIT, producer))
            
    def rapper_spots_left(self):
        return self.RAPPER_LIMIT - len(self.rappers)
    
    def producer_spots_left(self):
        return self.PRODUCER_LIMIT - len(self.producers)
        
    def is_valid(self):
        if (len(self.producers) > 0) and (len(self.producers) <= self.PRODUCER_LIMIT) \
            and (len(self.rappers) > 0) and (len(self.rappers) <= self.RAPPER_LIMIT):
              return True
        return False
        
    def weight(self):
        """
        Returns a score or weight of how "ideal" this team is between 0 and 1.
        
        An ideal team is not only valid, but has a 2 rappers and 2 producers.
        
        Less ideal (but valid) teams are.
        
        - 3 rappers and 2 producers
        - 2 rappers and 1 producer
        - 1 rapper and 2 producers
        - 1 rapper and 1 producer
        """
        # TODO: Calculate weighting score here
        return 1.0
    
    def __unicode__(self):
        return str({'rappers': self.rappers, 'producers': self.producers})
        
    def __repr__(self):
        return self.__unicode__()
    
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__