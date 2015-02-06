%define	debug_package	%nil
Name:		couturier 
Summary:	Merge PDF in LINUX
Version:	0.5
Release:	2
Source0:	http://dl.dropbox.com/u/1111373/Couturier/Karmic/%name-%version.tar.gz 
URL:		http://sites.google.com/site/couturierapp/
Group:		Office 
License:	GPLv3
BuildRequires:	mono-devel
BuildRequires:	gnome-sharp2-devel
BuildRequires:	glade-sharp2
	
%description
Couturier is a PDF merge application for the GNOME Desktop. 
It allows to merge multiple documents like PDF or images 
into one single PDF document

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files 
%_bindir/%name
%_libdir/%name
%_libdir/pkgconfig/%name.core.pc
%_datadir/applications/%name.desktop
