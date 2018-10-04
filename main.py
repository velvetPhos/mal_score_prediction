from tkinter import *
from tkinter.ttk import *
from anime_dataframe_creation import create_df
from anime_train_test_creation import create_train_test
from anime_score_prediction import predict_score
from result_combining import combine_results
from result_labeling import lable_result
from fscores_combining import combine_fscores

class mainApp:
    def __init__(self, app):
        self.app = app
        app.title("MAL Score Prediction App")

        app.geometry('500x300')
        app.resizable(False, False)

        background_image= PhotoImage(file="img.png")
        background_label = Label(app, image=background_image)
        background_label.place(x=-1, y=-1, relwidth=1, relheight=1)


        # cordinates are hard-coded because widget size output is inaccurate
        x_offset = 60

        y_offset = 40

        lbl1 = Label(app, text="Username:")
        lbl1.place(x=x_offset, y=y_offset)

        username = Entry(app,width=12)
        username.place(x=x_offset+73, y=y_offset-3)


        def deselect_all():
            ptw_var.set(0)
            dropped_var.set(0)
            hold_var.set(0)
            watching_var.set(0)

        def deselect_one():
            all_state_var.set(0)


        all_state_var = BooleanVar()
        all_state_var.set(True)
        all_state = Checkbutton(app, text='Select All', var=all_state_var, command=deselect_all)
        all_state.place(x=x_offset, y=y_offset + 25)

        ptw_var = BooleanVar()
        ptw_var.set(False)
        ptw = Checkbutton(app, text='PTW', var=ptw_var, command=deselect_one)
        ptw.place(x=x_offset+(111-25), y=y_offset + 25)

        dropped_var = BooleanVar()
        dropped_var.set(False)
        dropped = Checkbutton(app, text='Dropped', var=dropped_var, command=deselect_one)
        dropped.place(x=x_offset+(167-25), y=y_offset + 25)

        watching_var = BooleanVar()
        watching_var.set(False)
        wathcing = Checkbutton(app, text='Watching', var=watching_var, command=deselect_one)
        wathcing.place(x=x_offset+(248-25), y=y_offset + 25)

        hold_var = BooleanVar()
        hold_var.set(False)
        hold = Checkbutton(app, text='On Hold', var=hold_var, command=deselect_one)
        hold.place(x=x_offset+(334-25), y=y_offset + 25)


        lbl2 = Label(app, text="Minimum No.- Genre:")
        lbl2.place(x=x_offset, y=y_offset + 52)

        genre_lim = Entry(app,width=12)
        genre_lim.place(x=x_offset+142, y=y_offset + 49)


        lbl3 = Label(app, text="Minimum No.- Studio:")
        lbl3.place(x=x_offset, y=y_offset + 77)

        studio_lim = Entry(app,width=12)
        studio_lim.place(x=x_offset+145, y=y_offset + 74)


        lbl4 = Label(app, text="Rounds:")
        lbl4.place(x=x_offset, y=y_offset + 102)

        rounds = Entry(app,width=12)
        rounds.place(x=x_offset+57, y=y_offset + 99)

        label_var = BooleanVar()
        label_var.set(True)
        label = Checkbutton(app, text='Label Result', var=label_var)
        label.place(x=x_offset, y=y_offset + 127)

        def clicked():
            ignore_consumption = []
            #['consuming', 'completed', 'on_hold', 'dropped', 'backlog']
            if not all_state_var.get():
                if not ptw_var.get():
                    ignore_consumption.append('backlog')
                if not dropped_var.get():
                    ignore_consumption.append('dropped')
                if not watching_var.get():
                    ignore_consumption.append('consuming')
                if not hold_var.get():
                    ignore_consumption.append('on_hold')

            create_df(username.get(), ignore_consumption)
            create_train_test(int(genre_lim.get()), int(studio_lim.get()))
            predict_score(int(rounds.get()))
            combine_results(int(rounds.get()))
            combine_fscores(int(rounds.get()))

            if label_var.get():
                lable_result()

            print('Finished all processes')

        btn = Button(app, text="Start Prediction", command=clicked)

        btn.place(x=180, y=220)






app = Tk()
myApp = mainApp(app)
app.mainloop()
