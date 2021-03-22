from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
      file_object = open(fname,'r')
      current_line = file_object.readline().rstrip('\n')
      while current_line!="":
            if current_line=="line":
                xyz = file_object.readline().rstrip('\n') #x1,y1,z1,x2,y2,z2 for line
                arr = xyz.split(" ")
                add_edge(points,int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3]),int(arr[4]),int(arr[5]))
            elif current_line=="ident":
                ident(transform)
            elif current_line=="scale":
                xyz = file_object.readline().rstrip('\n')
                arr = xyz.split(" ")
                print(arr)
                sx=int(arr[0])
                sy=int(arr[1])
                sz=int(arr[2])
                scale_matrix=make_scale(sx,sy,sz)
                print(scale_matrix)
                matrix_mult(scale_matrix,transform)
            elif current_line=="move":#translate
                xyz = file_object.readline().rstrip('\n')
                arr = xyz.split(" ")
                tx=int(arr[0])
                ty=int(arr[1])
                tz=int(arr[2])
                translation_matrix=make_translate(tx,ty,tz)
                matrix_mult(translation_matrix,transform)
            elif current_line=="rotate":
                xyz = file_object.readline().rstrip('\n')
                arr = xyz.split(" ")
                axis=arr[0]
                theta=int(arr[1])
                if axis=="x":
                    rotation_matrix =make_rotX(theta)
                elif axis=="y":
                    rotation_matrix=make_rotY(theta)
                elif axis=="z":
                    rotation_matrix=make_rotZ(theta)
                matrix_mult(rotation_matrix,transform)
            elif current_line=="apply":
                matrix_mult(transform,points)
            elif current_line=="display":
                clear_screen(screen)
                print(points)
                draw_lines(points, screen, color)
                display(screen)
            elif current_line=="save":
                clear_screen(screen)
                draw_lines(points, screen, color)
                resulting_file=file_object.readline().rstrip('\n')
                save_ppm(screen,resulting_file)
            elif current_line=="quit":
                break
            current_line = file_object.readline().rstrip('\n')
      file_object.close()