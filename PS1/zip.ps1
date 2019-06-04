#get the list of files in the original folder
$rootFolder = "C:\Users\UnicornHGO\Desktop\files"
$destinationFolder = "C:\Users\UnicornHGO\Desktop"
$tempVariable = $rootFolder
$files = Get-ChildItem -Path $rootFolder 

#create a temporary folder using today's date
$tempFolderRoot = "C:\Temp_"
$date = Get-Date
$date = $date.ToString("yyyy-MM-dd")
$tempFinalFolder = "$tempFolderRoot$date"
New-Item -ItemType directory -Path $tempFinalFolder -Force

#decide how long back to go
$timespan = new-timespan -days 7

#move the files to a temporary location
foreach($file in $files)
{
	$fileLastModifieddate = $file.LastWriteTime
	if(((Get-Date) - $fileLastModifiedDate) -gt $timespan)
	{
		Move-Item "$rootFolder\$file" -destination $tempFinalFolder
	}
}

$CompressionToUse = [System.IO.Compression.CompressionLevel]::Optimal
$IncludeBaseFolder = $false
$zipTo = "$destinationFolder\Archive_{1}.zip" -f $rootFolder,$date

#add the files in the temporary location to a zip folder
[Reflection.Assembly]::LoadWithPartialName( "System.IO.Compression.FileSystem" )
[System.IO.Compression.ZipFile]::CreateFromDirectory($tempFinalFolder, $ZipTo, $CompressionToUse, $IncludeBaseFolder)

Remove-Item $tempFinalFolder -RECURSE