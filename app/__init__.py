import os,sys

root_path = [os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
                )
        )]

sys.path += root_path
