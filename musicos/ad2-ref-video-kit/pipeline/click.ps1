param([int]$x,[int]$y,[string]$shot="")
$code='using System; using System.Runtime.InteropServices; public class M { [DllImport("user32.dll")] public static extern bool SetCursorPos(int x,int y); [DllImport("user32.dll")] public static extern void mouse_event(uint f,uint x,uint y,uint d,UIntPtr e); }'
Add-Type -TypeDefinition $code
[M]::SetCursorPos($x,$y); Start-Sleep -Milliseconds 120
[M]::mouse_event(2,0,0,0,[UIntPtr]::Zero); Start-Sleep -Milliseconds 80; [M]::mouse_event(4,0,0,0,[UIntPtr]::Zero)
if($shot){ Start-Sleep -Milliseconds 900; Add-Type -AssemblyName System.Windows.Forms,System.Drawing; $b=[System.Windows.Forms.Screen]::PrimaryScreen.Bounds; $bmp=New-Object System.Drawing.Bitmap $b.Width,$b.Height; $g=[System.Drawing.Graphics]::FromImage($bmp); $g.CopyFromScreen($b.Location,[System.Drawing.Point]::Empty,$b.Size); $bmp.Save($shot) }
