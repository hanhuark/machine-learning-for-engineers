Add-Type -AssemblyName System.Drawing

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$coldPlate = [System.Drawing.Image]::FromFile((Join-Path $scriptRoot 'source/two-tier-cold-plate.png'))
$bubbleId = [System.Drawing.Image]::FromFile((Join-Path $scriptRoot 'source/bubbleid-inference.png'))
$canvas = New-Object System.Drawing.Bitmap 1280, 640
$graphics = [System.Drawing.Graphics]::FromImage($canvas)

try {
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $graphics.Clear([System.Drawing.Color]::FromArgb(8, 20, 32))

    $accent = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(71, 190, 214))
    $white = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(240, 245, 247))
    $muted = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(165, 185, 194))
    $line = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(75, 125, 146), 2)
    $titleFont = New-Object System.Drawing.Font 'Aptos Display', 33, ([System.Drawing.FontStyle]::Bold)
    $subtitleFont = New-Object System.Drawing.Font 'Aptos', 14, ([System.Drawing.FontStyle]::Regular)
    $labelFont = New-Object System.Drawing.Font 'Aptos', 12, ([System.Drawing.FontStyle]::Bold)

    $graphics.FillRectangle($accent, 54, 54, 8, 104)
    $graphics.DrawString('MACHINE LEARNING', $titleFont, $white, 82, 50)
    $graphics.DrawString('FOR ENGINEERS', $titleFont, $white, 82, 91)
    $graphics.DrawString('PHYSICAL SYSTEMS  |  EXPERIMENTAL DATA  |  VERIFICATION', $subtitleFont, $muted, 84, 143)
    $graphics.DrawLine($line, 54, 184, 1226, 184)

    $plateDestination = New-Object System.Drawing.Rectangle 40, 205, 520, 400
    $graphics.DrawImage($coldPlate, $plateDestination)
    $graphics.DrawString('TWO-TIER COLD PLATE', $labelFont, $muted, 54, 602)

    $boilingPanel = New-Object System.Drawing.Rectangle 635, 218, 590, 360
    $graphics.FillRectangle((New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(18, 36, 50))), $boilingPanel)
    $graphics.DrawImage($bubbleId, $boilingPanel)
    $graphics.DrawRectangle($line, $boilingPanel)
    $graphics.DrawString('BUBBLEID: DETECTION AND SEGMENTATION', $labelFont, $muted, 635, 602)

    $canvas.Save((Join-Path $scriptRoot 'machine-learning-for-engineers-social-preview.png'), [System.Drawing.Imaging.ImageFormat]::Png)
}
finally {
    if ($titleFont) { $titleFont.Dispose() }
    if ($subtitleFont) { $subtitleFont.Dispose() }
    if ($labelFont) { $labelFont.Dispose() }
    if ($line) { $line.Dispose() }
    if ($accent) { $accent.Dispose() }
    if ($white) { $white.Dispose() }
    if ($muted) { $muted.Dispose() }
    if ($graphics) { $graphics.Dispose() }
    if ($canvas) { $canvas.Dispose() }
    if ($coldPlate) { $coldPlate.Dispose() }
    if ($bubbleId) { $bubbleId.Dispose() }
}
