from PIL import Image


class View_terms_and_conditions():
    def run_t_and_c(self):
        with open('C:/Users/aosbo/PycharmProjects/Sparta_Airport_Project/Airport/1.jpg', "rb") as picture:
            pic = picture.read()
            Image.open("C:/Users/aosbo/PycharmProjects/Sparta_Airport_Project/Airport/1.jpg").show()


    # def read_image_file(self):
    #     with open('sasuke.png', 'rb') as picture, open("sasuke_out.png", "wb") as picture2:
    #         pic = picture.read()
    #         picture2.write(pic)
    #         Image.open("sasuke_out.png").show()