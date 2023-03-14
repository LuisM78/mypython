import subprocess  # IMPORT FOR SUB PROCESS . RUN METHOD
import sys



filename0 = sys.argv[0]
filename2 = sys.argv[1]

print('filename2', filename2)
POWERSHELL_PATH = "powershell.exe"  # POWERSHELL EXE PATH
ps_script_path = "C:\\Users\\v-luiscan\\Documents\\mypython\\mypower.ps1"  # YOUR POWERSHELL FILE PATH


class Utility:  # SHARED CLASS TO USE IN OUR PROJECT

    @staticmethod    # STATIC METHOD DEFINITION
    def run_ftp_upload_powershell_script(script_path, *params):  # SCRIPT PATH = POWERSHELL SCRIPT PATH,  PARAM = POWERSHELL SCRIPT PARAMETERS ( IF ANY )

        commandline_options = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', script_path]  # ADD POWERSHELL EXE AND EXECUTION POLICY TO COMMAND VARIABLE
        for param in params:  # LOOP FOR EACH PARAMETER FROM ARRAY
            commandline_options.append("'" + param + "'")  # APPEND YOUR FOR POWERSHELL SCRIPT

        process_result = subprocess.run(commandline_options, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)  # CALL PROCESS
        print('return code')
        print(process_result.returncode)  # PRINT RETURN CODE OF PROCESS  0 = SUCCESS, NON-ZERO = FAIL  
        print('***')
        
        print(process_result.stdout)      # PRINT STANDARD OUTPUT FROM POWERSHELL
        print(process_result.stderr)      # PRINT STANDARD ERROR FROM POWERSHELL ( IF ANY OTHERWISE ITS NULL|NONE )

        if process_result.returncode == 0:  # COMPARING RESULT
            Message = "Success !"
        else:
            Message = "Error Occurred !"


        return Message  # RETURN MESSAGE

A = Utility()
result = A.run_ftp_upload_powershell_script(ps_script_path,'hello','world')
print('result message ',result)

ps_script_path2 = "C:\\Users\\v-luiscan\\Documents\\mypython\\powershl2.ps1"

#print('fhe file name is = ', filename)
A = Utility()
result = A.run_ftp_upload_powershell_script(ps_script_path2,"5","C:\\Users\\v-luiscan\\Documents\\mypython\\mytrial copy.txt")
#result = A.run_ftp_upload_powershell_script(ps_script_path2,"5",filename2)
