from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import Button, Tk, Label, Canvas

def openCardCallback(layout,front_card,mom_img,mom_flipped_img,mom_field_img,sig_message_img,quote_img):
    """
    Runs code to display images to wish mom a happy mother's day
    front_card - the image already displayed in the front of the card
    """

    #Remove from card image
    layout.delete(front_card)

    #Display picture of mom
    mom_field = layout.create_image(325,0,anchor='nw',image=mom_field_img)

    #Move on to next step of card - mom dancing in the leaves
    layout.after(3000,lambda: display_mom(layout,mom_field,mom_img,mom_flipped_img,sig_message_img,quote_img))
    
    

def display_mom(layout,mom_field,mom_img,mom_flipped_img,sig_message_img,quote_img):
    """
    Display mom dancing in the leaves
    """
    layout.delete(mom_field)

    mom = layout.create_image(325,345,anchor='nw',image=mom_img)

    times=10
    layout.after(3000,lambda: create_dancing(layout,mom_img,mom_flipped_img,times,times,True,mom))

    #After 3 seconds display a message on card
    layout.after(1000*times+4000,lambda: display_message(layout,sig_message_img,quote_img))


def create_dancing(layout,mom_img,mom_flipped_img,times_to_run,total_times,flip,last_image):
    """
    Create mom dancing in the leaves
    """

    if times_to_run>0:
        layout.delete(last_image)
        if flip:
            last_image = layout.create_image(325+100*(total_times-times_to_run),345,anchor='nw',image=mom_flipped_img)
        else:
            last_image = layout.create_image(325+100*(total_times-times_to_run),345,anchor='nw',image=mom_img)

        create_leaves(layout,325+100*(total_times-times_to_run),100,False)
        create_leaves(layout,400+100*(total_times-times_to_run),150,True)
        create_leaves(layout,325+100*(total_times-times_to_run),200,False)

        times_to_run-=1
        layout.after(1000,lambda: create_dancing(layout,mom_img,mom_flipped_img,times_to_run,total_times,not flip,last_image))

def display_message(layout,sig_message_img,quote_img):
    """
    Display message for mom!
    """
    #Create message for card
    sig_message = layout.create_image(325,150,anchor='nw',image=sig_message_img)
    
    #After 3 seconds remove message and display a quote
    layout.after(7000,lambda: display_quote(layout,sig_message,quote_img))


def display_quote(layout,sig_message,quote_img):
    """
    Display a quote from Nhat Hanh
    """
    layout.delete(sig_message)

    #Create quote for the card
    layout.create_image(325,150,anchor='nw',image=quote_img)


def create_leaves(layout,x1,y1,flipped):
    """
    Create the leaves in the image tk
    """
    #Points to define outline of leaf
    points = []

    length = 5
    down_slope_temp = [6.75,6.5,6,5,3,0]
    down_slope = [i*length for i in down_slope_temp]

    if flipped:
        for i in range(len(down_slope)):
            points.append((x1+i*length,y1+down_slope[i]))
        
        for i in range(len(down_slope)):
            points.append((x1+(len(down_slope)-i-1)*length,y1+down_slope[-1]-down_slope[i]))

    else:
        down_slope.sort()
        for i in range(len(down_slope)):
            points.append((x1+i*length,y1+down_slope[i]))
        
        for i in range(len(down_slope)):
            points.append((x1+(len(down_slope)-i-1)*length,y1+down_slope[-1]-down_slope[i]))

    layout.create_polygon(points,outline='brown',fill='green')
    




if __name__ == '__main__':
    
    #Create a tkinter window
    root = Tk()
    root.geometry('1500x800')

    #Create a card using PIL
    width = 20
    box = (0,0,700,500)
    fancy_font = ImageFont.truetype('C:/Windows/Fonts/SCRIPTBL.ttf',70)
    fancy_font_small = ImageFont.truetype('C:/Windows/Fonts/SCRIPTBL.ttf',35)

    #Create a image for the front of the card
    card = Image.new('RGBA',(800,600),(0,0,0,0))
    draw = ImageDraw.Draw(card)
    draw.rectangle(box,fill="purple",outline="yellow")
    draw.rectangle((box[0]+width,box[1]+width,box[2]-width,box[3]-width),fill="yellow")
    draw.text((250,80),"Happy",font=fancy_font,fill="purple")
    draw.text((225,200),"Mother's",font=fancy_font,fill="purple")
    draw.text((275,320),"Day!",font=fancy_font,fill="purple")
    front_card_img = ImageTk.PhotoImage(card)

    #Mom picture for card
    load_mom_field = Image.open('Mom_Field.jpg')
    mom_field_img = ImageTk.PhotoImage(load_mom_field)

    #Mom image for card
    load_mom = Image.open('Mom.jpg')
    mom_img = ImageTk.PhotoImage(load_mom)

    #Flip picture of mom
    load_mom_flipped = load_mom.transpose(Image.FLIP_LEFT_RIGHT)
    mom_flipped_img = ImageTk.PhotoImage(load_mom_flipped)

    #Create message for card
    message = Image.new('RGBA',(800,600),(0,0,0,0))
    draw_message = ImageDraw.Draw(message)
    draw_message.rectangle(box,fill="purple",outline="yellow")
    draw_message.rectangle((box[0]+width,box[1]+width,box[2]-width,box[3]-width),fill="yellow")
    draw_message.text((150,80),"May your heart be filled",font=fancy_font_small,fill="purple")
    draw_message.text((150,140),"with the beauty of nature,",font=fancy_font_small,fill="purple")
    draw_message.text((150,200),"and your spirit dance",font=fancy_font_small,fill="purple")
    draw_message.text((150,260),"in celebration of life.",font=fancy_font_small,fill="purple")
    draw_message.text((175,350),"- Your son, Chris",font=fancy_font_small,fill="purple")
    sig_message_img = ImageTk.PhotoImage(message)

    #Create a quote for the card
    quote = Image.new('RGBA',(800,600),(0,0,0,0))
    draw_quote = ImageDraw.Draw(quote)
    draw_quote.rectangle(box,fill="purple",outline="yellow")
    draw_quote.rectangle((box[0]+width,box[1]+width,box[2]-width,box[3]-width),fill="yellow")
    draw_quote.text((50,100),"Walk as if your feet",font=fancy_font,fill="purple")
    draw_quote.text((75,170),"are kissing the Earth.",font=fancy_font,fill="purple")
    draw_quote.text((65,300),"- Nhat Hanh",font=fancy_font,fill="purple")
    quote_img = ImageTk.PhotoImage(quote)
    
    #Create a canvas to add images
    layout_width = 1500
    layout_height = 800
    layout = Canvas(root,width=layout_width,height=layout_height)
    layout.pack()

    #Add front image to card
    front_card = layout.create_image(325,150,anchor='nw',image=front_card_img)

    #Create buttons for mom to press
    close_button = Button(root,text='Close',bd='30',command=root.destroy)
    layout.create_window(100,500,anchor='nw',window=close_button)
    open_button = Button(root,text='Open Card',bd='30',command=lambda: openCardCallback(layout,front_card,mom_img,mom_flipped_img,mom_field_img,sig_message_img,quote_img))
    layout.create_window(100,300,anchor='nw',window=open_button)
    
    root.mainloop()

    mom_field = Image.open("Mom_Field.jpg")
    mom = Image.open("Mom.jpg")







