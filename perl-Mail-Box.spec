%define	module Mail-Box
%define	name	perl-%{module}
%define	version	2.065
%define	release	1mdk

Summary:	Mail-folder manager API
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
# workaround perl automatic dependencies which fail to grab this one
Provides:	perl(Mail::Message::Construct)
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Mail-MboxParser
BuildRequires:	perl-File-Remove
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-Mail-SpamAssassin
BuildRequires:	perl-Mail-IMAPClient
BuildRequires:	perl-User-Identity
BuildRequires:	perl-MailTools
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Object-Realize-Later
BuildRequires:	perl-HTML-Format
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Mail::Box folder is a modern mail-folder manager. It is written to replace
Mail::Folder, although it interface is different.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

# fix permissions
find %{buildroot} -type f -exec chmod 0644 {} \;
find %{buildroot} -type d -exec chmod 0755 {} \;

# remove unused file
rm -f %{buildroot}%{perl_vendorlib}/Mail/Makefile.PL

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE README* TODO.v2
%{_mandir}/*/*
%{perl_vendorlib}/Mail

