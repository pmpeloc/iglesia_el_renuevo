param([string]$text,[int]$backspaces=40)
$c='using System; using System.Runtime.InteropServices; public class WK2 { [DllImport("user32.dll")] public static extern IntPtr FindWindow(string c, string t); [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr h, uint m, IntPtr w, IntPtr l); [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow(); }'
Add-Type -TypeDefinition $c
$h=[WK2]::FindWindow([NullString]::Value,"XLN Audio - Addictive Drums 2"); "hwnd $h fg $([WK2]::GetForegroundWindow())"
$WM_KEYDOWN=0x100; $WM_KEYUP=0x101; $WM_CHAR=0x102
[WK2]::PostMessage($h,$WM_KEYDOWN,[IntPtr]0x23,[IntPtr]0) | Out-Null; [WK2]::PostMessage($h,$WM_KEYUP,[IntPtr]0x23,[IntPtr]0) | Out-Null  # END
for($i=0;$i -lt $backspaces;$i++){ [WK2]::PostMessage($h,$WM_KEYDOWN,[IntPtr]0x08,[IntPtr]0) | Out-Null; [WK2]::PostMessage($h,$WM_CHAR,[IntPtr]0x08,[IntPtr]0) | Out-Null; [WK2]::PostMessage($h,$WM_KEYUP,[IntPtr]0x08,[IntPtr]0) | Out-Null }
foreach($ch in $text.ToCharArray()){ [WK2]::PostMessage($h,$WM_CHAR,[IntPtr][int][char]$ch,[IntPtr]0) | Out-Null; Start-Sleep -Milliseconds 15 }
"typed"
