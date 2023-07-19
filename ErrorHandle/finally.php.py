#runs without an error

try:
    f = open("testfile",'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("There was a OS Error")
finally:
    print("I always run")

#runs with an error


try:
    f = open("testfile5",'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("There was a OS Error")
except:
    print("All other type of error")
finally:
    print("I always run")