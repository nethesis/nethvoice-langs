Name:		nethvoice-lang
Version: 2.0.1
Release: 1%{?dist}
Summary:	language packages for NethVoice
Group:		Networking/Daemons
License:	GPL
Source:      %{name}-%{version}.tar.gz
# Italian
Source10:    https://github.com/nethesis/nethvoice-langs/releases/download/2.0.0/asterisk-sounds-core-it-2.11.1.zip
Source1:     https://github.com/nethesis/nethvoice-langs/releases/download/2.0.0/asterisk-sounds-extra-it-2.11.1.zip
# Spanish
Source2:    https://www.asterisksounds.org/sites/asterisksounds.org/files/sounds/es-ES/download/asterisk-sounds-core-es-ES-2.9.15.zip
Source3:    https://www.asterisksounds.org/sites/asterisksounds.org/files/sounds/es-ES/download/asterisk-sounds-extra-es-ES-2.9.15.zip
# French
Source4:    https://www.asterisksounds.org/sites/asterisksounds.org/files/sounds/fr-FR/download/asterisk-sounds-core-fr-FR-2.3.10.zip
Source5:    https://www.asterisksounds.org/sites/asterisksounds.org/files/sounds/fr-FR/download/asterisk-sounds-extra-fr-FR-2.3.10.zip
# German
Source6:    https://www.asterisksounds.org/sites/asterisksounds.org/files/sounds/de/download/asterisk-sounds-core-de-2.11.19.zip
Source7:    https://www.asterisksounds.org/sites/asterisksounds.org/files/sounds/de/download/asterisk-sounds-extra-de-2.11.19.zip
# English
Source8:    https://github.com/nethesis/nethvoice-langs/releases/download/2.0.0/asterisk-sounds-core-en-2.11.1.zip
Source9:    https://github.com/nethesis/nethvoice-langs/releases/download/2.0.0/asterisk-sounds-extra-en-2.11.1.zip

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires: nethserver-devtools
Requires: nethserver-nethvoice

%description
Language packs from www.asterisksounds.org packaged for NethVoice. 

%package en
Summary: English language for Asterisk
Group: Utilities/System
%description en
English language pack from www.asterisksounds.org packaged for NethVoice. 

%package it
Summary: Italian language for Asterisk
Group: Utilities/System
%description it
Italian language pack from www.asterisksounds.org packaged for NethVoice. 

%package es
Summary: Spanish language for Asterisk
Group: Utilities/System
%description es
Spanish language pack from www.asterisksounds.org packaged for NethVoice.

%package fr
Summary: French language for Asterisk
Group: Utilities/System
%description fr
French language pack from www.asterisksounds.org packaged for NethVoice.

%package de
Summary: German language for Asterisk
Group: Utilities/System
%description de
German language pack from www.asterisksounds.org packaged for NethVoice.

%prep
%setup
for LANG in $(ls %{_sourcedir}/asterisk-sounds* | cut -d- -f4 | sort -u); do
    mkdir -p %{_sourcedir}/$LANG
    for FILE in $(ls %{_sourcedir}/asterisk-sounds-*-$LANG-*.zip); do
        unzip -o $FILE -d %{_sourcedir}/$LANG
    done
done

%build

%install
rm -rf $RPM_BUILD_ROOT
for LANG in $(ls %{_sourcedir}/asterisk-sounds* | cut -d- -f4 | sort -u); do
    mkdir -p ${RPM_BUILD_ROOT}/var/lib/asterisk/sounds/$LANG
    mkdir -p ${RPM_BUILD_ROOT}/var/lib/asterisk/sounds/$LANG/custom
    cp -a %{_sourcedir}/$LANG/* ${RPM_BUILD_ROOT}/var/lib/asterisk/sounds/$LANG
done

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files it
%defattr(-, root, root)
/var/lib/asterisk/sounds/it/*
%attr(0755,asterisk,asterisk) %dir /var/lib/asterisk/sounds/it/custom
%doc COPYING

%files en
%defattr(-, root, root)
/var/lib/asterisk/sounds/en/*
%attr(0755,asterisk,asterisk) %dir /var/lib/asterisk/sounds/en/custom

%files es
%defattr(-, root, root)
/var/lib/asterisk/sounds/es/*
%attr(0755,asterisk,asterisk) %dir /var/lib/asterisk/sounds/es/custom

%files de
%defattr(-, root, root)
/var/lib/asterisk/sounds/de/*
%attr(0755,asterisk,asterisk) %dir /var/lib/asterisk/sounds/de/custom

%files fr
%defattr(-, root, root)
/var/lib/asterisk/sounds/fr/*
%attr(0755,asterisk,asterisk) %dir /var/lib/asterisk/sounds/fr/custom

%changelog
* Mon Feb 14 2022 Stefano Fancello <stefano.fancello@nethesis.it> - 2.0.1-1
- NethVoice new voice recording has a "click" when recording is started - Bug nethesis/dev#6111

* Mon Dec 06 2021 Stefano Fancello <stefano.fancello@nethesis.it> - 2.0.0-1
- Use professional voices for English and Italian audio files - nethesis/dev#6085

* Mon Nov 11 2019 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.1-1
- add missing no-valid-responce-transfering file nethesis/dev#5715

* Tue Mar 26 2019 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- Use italian sounds generated with Google Wavenet TTS nethesis/dev#5594

* Fri Feb 16 2018 Stefano Fancello <stefano.fancello@nethesis.it> - 1.0.1-1
- Create custom sound directory to allow users to save custom recordings nethesis/dev#5332

* Thu Aug 31 2017 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0.0-1
Release 1.0.0


