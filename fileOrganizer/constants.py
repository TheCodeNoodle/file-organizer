FOLDERS = ["Videos", "Pictures", "Zip", "Documents", "Programs", "Music", "Other"]

MUSIC_EXTENSIONS = [
    # Lossless formats
    ".flac", ".alac", ".wav", ".aiff", ".dsd", ".dsf", ".dff",
    # Lossy compressed formats
    ".mp3", ".aac", ".m4a", ".ogg", ".opus", ".wma", ".amr",
    # Less common formats
    ".ape", ".tak", ".tta", ".wv", ".mpc", ".ac3", ".dts",
    # Tracker/module formats
    ".mod", ".s3m", ".xm", ".it", ".med", ".stm",
    # MIDI and sheet music
    ".mid", ".midi", ".kar", ".mus", ".mxl"
]

PROGRAM_EXTENSIONS = [
    # Windows executables
    ".exe", ".msi", ".bat", ".cmd", ".com", ".scr", ".pif", 
    ".cpl", ".gadget", ".vb", ".vbs", ".js", ".jse", ".wsf", ".wsh",
    # Unix/Linux executables
    ".sh", ".bash", ".zsh", ".fish", ".csh", ".ksh", ".run", ".bin",
    # Programming languages
    ".py", ".pyw", ".pyc", ".pyo", ".pyd", ".rb", ".pl", ".pm",
    ".php", ".lua", ".tcl", ".r", ".m", ".go", ".rs",
    # Java/JVM
    ".jar", ".class", ".war", ".ear", ".jnlp",
    # Mobile apps
    ".apk", ".ipa", ".xap", ".appx", ".msix",
    # Package managers
    ".deb", ".rpm", ".pkg", ".dmg", ".app", ".flatpak", ".snap",
    # Installer formats
    ".nsis", ".inno", ".wise", ".installshield"
]

DOCUMENT_EXTENSIONS = [
    # Text documents
    ".txt", ".rtf", ".md", ".markdown", ".rst", ".asciidoc", ".textile",
    ".log", ".readme", ".1st", ".diz", ".nfo",
    # Microsoft Office
    ".doc", ".docx", ".docm", ".dot", ".dotx", ".dotm",
    ".xls", ".xlsx", ".xlsm", ".xlt", ".xltx", ".xltm", ".xlsb",
    ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm", ".pps", ".ppsx", ".ppsm",
    # OpenDocument formats
    ".odt", ".ods", ".odp", ".odg", ".odf", ".odb", ".odc", ".odm",
    # Adobe formats
    ".pdf", ".ai", ".ps", ".eps", ".indd", ".idml",
    # E-book formats
    ".epub", ".mobi", ".azw", ".azw3", ".fb2", ".lit", ".pdb", ".tcr",
    # Spreadsheet and data
    ".csv", ".tsv", ".ods", ".numbers", ".gnumeric",
    # Presentation formats
    ".key", ".odp", ".sxi", ".sti",
    # Publishing and typesetting
    ".tex", ".latex", ".bib", ".cls", ".sty", ".dtx", ".ins",
    ".wpd", ".wps", ".pages", ".pub", ".qxd", ".pm6", ".pmd",
    # Other formats
    ".chm", ".hlp", ".man", ".info", ".texinfo"
]

ZIP_EXTENSIONS = [
    # Common archives
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".lz", ".lzma",
    ".tgz", ".tbz", ".tbz2", ".txz", ".tlz",
    # Specialized archives
    ".z", ".arj", ".lzh", ".lha", ".ace", ".cab", ".sea", ".sit", ".sitx",
    ".zoo", ".arc", ".pak", ".paq", ".pea", ".quad", ".balz",
    # Image archives
    ".iso", ".img", ".bin", ".cue", ".mdf", ".mds", ".nrg", ".cdi",
    ".dmg", ".toast", ".vcd", ".udf",
    # Package formats
    ".deb", ".rpm", ".pkg", ".xar", ".wim", ".swm", ".esd",
    # Backup formats
    ".bkf", ".bkz", ".bz", ".tbk", ".vbk", ".ghb", ".nb7", ".nbd",
    # Other compressed formats
    ".torrent", ".crx", ".xpi", ".oex", ".safariextz"
]

VIDEO_EXTENSIONS = [
    # Common video formats
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",
    ".mpg", ".mpeg", ".m4v", ".3gp", ".3g2",
    # High quality formats
    ".mts", ".m2ts", ".ts", ".mxf", ".r3d", ".braw", ".arw",
    # Old/legacy formats
    ".asf", ".rm", ".rmvb", ".vob", ".ogv", ".dv", ".amv",
    # Streaming formats
    ".f4v", ".f4p", ".f4a", ".f4b", ".m3u8", ".mpd",
    # Professional formats
    ".prores", ".dnxhd", ".cineform", ".avchd", ".xavc",
    # Animation formats
    ".swf", ".fla", ".gif", ".apng", ".mng",
    # Subtitle files (often grouped with videos)
    ".srt", ".sub", ".idx", ".vtt", ".ass", ".ssa", ".smi", ".rt"
]

PICTURE_EXTENSIONS = [
    # Common raster formats
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
    ".webp", ".heic", ".heif", ".avif", ".jxl",
    # Raw camera formats
    ".raw", ".cr2", ".cr3", ".nef", ".arw", ".orf", ".rw2",
    ".pef", ".srw", ".x3f", ".raf", ".3fr", ".fff", ".mef",
    ".mos", ".nrw", ".ptx", ".pxn", ".r3d",
    # Vector formats
    ".svg", ".eps", ".ai", ".cdr", ".wmf", ".emf", ".cgm",
    # Professional formats
    ".psd", ".psb", ".xcf", ".kra", ".ora", ".clip", ".sai2",
    ".mdp", ".pdn", ".afdesign", ".afphoto",
    # Web formats
    ".ico", ".cur", ".ani", ".icns", ".favicon",
    # Old/legacy formats
    ".pcx", ".tga", ".dds", ".hdr", ".exr", ".pic", ".pict",
    ".sgi", ".iff", ".lbm", ".pbm", ".pgm", ".ppm", ".pnm",
    # Medical/scientific
    ".dcm", ".dicom", ".nii", ".img", ".hdr",
    # Other specialized
    ".jp2", ".jpx", ".j2k", ".djvu", ".djv", ".wbmp", ".xbm", ".xpm"
]
