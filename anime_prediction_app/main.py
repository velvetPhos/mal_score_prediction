from tkinter import *
from tkinter.ttk import *

from alist_fetch import get_alist
from merge_alist import merge_alist
from database_fetch import update_data
from anime_train_test_creation import create_train_test
from anime_score_prediction import predict_score
from result_combining import combine_results
from fscores_combining import combine_fscores
from result_labeling import lable_result

class mainApp:
    def __init__(self, app):
        self.app = app
        app.title("MAL Score Prediction App")

        app.geometry('300x200')
        app.resizable(False, False)

        background_image= PhotoImage(file="img.png")
        background_label = Label(app, image=background_image)
        background_label.place(x=-1, y=-1, relwidth=1, relheight=1)


        # cordinates are hard-coded because widget size output is inaccurate
        x_offset = 50

        y_offset = 40

        lbl1 = Label(app, text="Username:")
        lbl1.place(x=x_offset, y=y_offset)

        username = Entry(app,width=12)
        username.place(x=x_offset+73, y=y_offset-3)

        lbl4 = Label(app, text="Rounds:")
        lbl4.place(x=x_offset, y=y_offset + 50)

        rounds = Entry(app,width=12)
        rounds.place(x=x_offset+57, y=y_offset + 47)


        def clicked():
            get_alist(username.get())
            merge_alist()
            update_data()
            create_train_test()
            predict_score(int(rounds.get()))
            combine_results(int(rounds.get()))
            lable_result()
            combine_fscores(int(rounds.get()))

            print('Finished all processes')

        btn = Button(app, text="Start Prediction", command=clicked)

        btn.place(x=x_offset+35, y=y_offset+100)






app = Tk()
myApp = mainApp(app)
app.mainloop()
