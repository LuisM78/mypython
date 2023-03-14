param(
    [Parameter(Mandatory=$True, Position=0, ValueFromPipeline=$false)]
    [System.String]
    $Param1,
    
    [Parameter(Mandatory=$True, Position=1, ValueFromPipeline=$false)]
    [System.String]
    $Param2
)

#$file = "file.txt"
#$file = "C:\\Users\\v-luiscan\\Documents\\mypython\\mytrial copy.txt"
# Get-Content $file | Measure-Object -Line
# $a = (Get-Content $file | Measure-Object)
# (Get-Content $file) | ? {($a.count-1)-notcontains $_.ReadCount} | Set-Content $file
$content = Get-Content $Param2
Write-Host $content.length
$content[0..($content.length-$Param1)]|Out-File $Param2 -Force

# Call the script like so from command line
# PS C:\Users\v-luiscan\Documents\mypython> .\powershl2.ps1 3 "C:\\Users\\v-luiscan\\Documents\\mypython\\mytrial copy.txt"