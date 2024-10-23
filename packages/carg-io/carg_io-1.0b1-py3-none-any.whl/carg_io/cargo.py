# from __future__ import annotations
# from typing import List
# from .core import ParameterSet
# import zipfile
# from pathlib import Path
# import tkinter as tk

# class Container:
#     """
#     A collection of i/o parameters and any result files.

#     This is an object-oriented datastorage, and propably pretty slow.
#     But for more intensive stuff, we might have a relational database equivalent

#     """

#     i:List[ParameterSet]
#     o:List[ParameterSet]

#     def __init__(self, input:List[ParameterSet]=[], output:List[ParameterSet]=[]):
#         self.input = input
#         self.output = output
#         self.additional_files = []
    
#     def append_file(self, file:Path|str):
#         self.additional_files.append(Path(file))

#     def append_input(self, input:ParameterSet):
#         self.input.append(input)
    
#     def append_output(self, output:ParameterSet):
#         self.output.append(output)

#     @staticmethod
#     def load(file:str, subclass:Container):
#         input, output = [], []
#         idict = {i.name:i for i in subclass.i}
#         odict = {o.name:o for o in subclass.o}
#         with zipfile.ZipFile(file, mode="r") as archive:
#             for file in archive.filelist:
#                 data = archive.read(file.filename)
#                 name, _ = file.filename.split('.')
                
#                 if name in idict:
#                     cls = idict[name]
#                     inst = cls.from_serial_pickle(data)
#                     input.append(inst)
#                 elif name in odict:
#                     cls = odict[name]
#                     inst = cls.from_serial_pickle(data)
#                     output.append(inst)
#                 else:
#                     pass #TODO
#         return subclass(input=input, output=output)

#     def save(self, file:Path):
#         with zipfile.ZipFile(file, mode="w") as archive:
#             for filename in self.additional_files:
#                 archive.write(filename)
            
#             for pset in self.input + self.output:
#                 filename = pset.to_pickle()
#                 archive.write(filename)
            
#     def file_ui(self):
#         root = tk.Tk()
        
#         input_column = tk.LabelFrame(root, text='INPUT', font=('Helvetica 10 bold'))
#         sbi = tk.Scrollbar(input_column, orient = 'vertical')
#         sbi.pack(side=tk.LEFT, fill=tk.Y)
#         input_parm = tk.Frame(input_column, width=360, height=520)
#         for inp in self.input:
#             frame, entries = inp._to_tk(input_parm, state='disabled')
#             frame.pack(padx=(10,10), pady=(10,10), side=tk.TOP)
        

#         output_column = tk.LabelFrame(root, text='OUTPUT', font=('Helvetica 10 bold'))
#         output_parm = tk.Frame(output_column, width=360, height=520)
#         for inp in self.output:
#             inp:ParameterSet
#             frame, entries = inp._to_tk(output_parm, state='disabled')
#             frame.pack(padx=(10,10), pady=(10,10), side=tk.TOP)
        
#         input_parm.pack(side=tk.TOP)
#         input_column.pack(side=tk.LEFT)
#         output_parm.pack(side=tk.TOP)
#         output_column.pack(side=tk.LEFT)
        

#         root.mainloop()


#     def get_partial_hash(self):
#         pass
    
#     def __hash__(self):
#         pass

#     def open(self):
#         pass


    

# class Vessel:
#     """
#     A collection of containers

#     """

#     def __init__(self, containers:List[Container]):
#         self.containers = containers

    

# class Database:
#     """
    
#     """
#     pass