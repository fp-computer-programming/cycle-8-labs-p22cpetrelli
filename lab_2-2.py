#author CJP (AMDG) 12/2/21
def inviting(lst):
    for name in lst:
        print("Hi {0}, You're invited to my party on Friday!".format(name))


inviting(['Cam', 'Jack', 'James'])