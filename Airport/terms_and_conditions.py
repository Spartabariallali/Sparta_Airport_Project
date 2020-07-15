from PIL import Image


class View_terms_and_conditions():
    def run_t_and_c(self):
        with open("AgileAirlines.png", "rb") as picture:
            pic = picture.read()
            Image.open("AgileAirlines.png")



    # def read_image_file(self):
    #     with open('sasuke.png', 'rb') as picture, open("sasuke_out.png", "wb") as picture2:
    #         pic = picture.read()
    #         picture2.write(pic)
    #         Image.open("sasuke_out.png").show()