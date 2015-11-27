# content of test_sample.py
def test_answer(slide_number):
    if slide_number == "Slide1":
        print "from test_answer {sn}".format(sn=slide_number)
    elif slide_number == "Slide2":
        print "from test_answer {sn}".format(sn=slide_number)
    #assert 0 # to see what was printed
