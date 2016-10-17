#!/bin/bash

# Install dependencies

if [ "$TRAVIS_OS_NAME" == "linux" ]; then

    sudo apt-get -qq update
    sudo apt-get install -y libpango1.0-dev libpangomm-1.4-dev build-essential \
                            autoconf automake autopoint intltool libtool libglib2.0-dev \
                            libpng12-dev libgc-dev libfreetype6-dev liblcms2-dev libgtkmm-2.4-dev \
                            libxslt1-dev libboost-dev libpopt-dev libgsl0-dev libaspell-dev \
                            libpoppler-dev libpoppler-glib-dev libssl-dev libwpg-dev libcdr-dev \
                            libvisio-dev potrace libpotrace-dev libgtkmm-3.0-dev libgtk3.0-cil-dev \
                            libgdl-3-dev libpoppler-cil-dev libpoppler-cpp-dev \
                            libpoppler-private-dev libgnome-vfs2.0-cil-dev git wget cmake

fi


if [ "$TRAVIS_OS_NAME" == "osx" ]; then

    brew update

    brew install cairo --with-glib
    brew install gtk+3 poppler python gdk-pixbuf gtkmm3 cairomm librsvg libsvg-cairo \
                 gdk-pixbuf pango pangomm argyll-cms intltool popt libxslt libwpd libwpg \
                 libcroco libxml2 gsl gdl gettext

fi

cmake --version
