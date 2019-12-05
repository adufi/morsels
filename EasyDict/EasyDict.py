class EasyDict(object):
    def __init__(self, *initial_data, **kwargs):
        # Add every attributes in a tmp dict
        tmp = {}
        for _dict in initial_data:
            for key in _dict:
                tmp[key] = _dict[key]

        for key in kwargs:
            tmp[key] = kwargs[key]

        # Look for a normalize key
        self.normalize = False
        if 'normalize' in tmp:
            self.normalize = tmp['normalize']

        # Sanity check
        # print(f'normalize: {self.normalize}')
        
        for _key in tmp:
            key = self.__rep(_key)
            # Sanity check
            # print (key)
            self.__dict__[key] = tmp[_key]            

    def __getitem__(self, key):
        return getattr(self, self.__rep(key))

    def __setitem__(self, key, value):
        setattr(self, self.__rep(key), value)

    def __contains__(self, key):
        return self.__rep(key) in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __eq__(self, other):
        for _key in self.__dict__:
            key = self.__rep(_key)

            if key not in other:
                return False
            if self.__dict__[key] != other[key]:
                return False
        return True

    def get(self, _value, default=None):
        value = self.__rep(_value)
        return self.__dict__.get(value, default)

    # Macro
    # Return non-space key if normalize is set to True 
    def __rep(self, key):
        return key.replace(' ', '_') if self.normalize else key
