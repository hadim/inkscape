# -----------------------------------------------------------------------------
# Define the main source
# -----------------------------------------------------------------------------

set(sp_SRC
  attribute-rel-css.cpp
  attribute-rel-svg.cpp
  attribute-rel-util.cpp
  attribute-sort-util.cpp
  sp-anchor.cpp
  sp-clippath.cpp
  sp-conn-end-pair.cpp
  sp-conn-end.cpp
  sp-cursor.cpp
  sp-defs.cpp
  sp-desc.cpp
  sp-ellipse.cpp
  sp-factory.cpp
  sp-filter-primitive.cpp
  sp-filter-reference.cpp
  sp-filter.cpp
  sp-flowdiv.cpp
  sp-flowregion.cpp
  sp-flowtext.cpp
  sp-font-face.cpp
  sp-font.cpp
  sp-glyph-kerning.cpp
  sp-glyph.cpp
  sp-gradient-reference.cpp
  sp-gradient.cpp
  sp-guide.cpp
  sp-hatch-path.cpp
  sp-hatch.cpp
  sp-image.cpp
  sp-item-group.cpp
  sp-item-notify-moveto.cpp
  sp-item-rm-unsatisfied-cns.cpp
  sp-item-transform.cpp
  sp-item-update-cns.cpp
  sp-item.cpp
  sp-line.cpp
  sp-linear-gradient.cpp
  sp-lpe-item.cpp
  sp-marker.cpp
  sp-mask.cpp
  sp-mesh-array.cpp
  sp-mesh-gradient.cpp
  sp-mesh-patch.cpp
  sp-mesh-row.cpp
  sp-metadata.cpp
  sp-missing-glyph.cpp
  sp-namedview.cpp
  sp-object-group.cpp
  sp-object.cpp
  sp-offset.cpp
  sp-paint-server.cpp
  sp-path.cpp
  sp-pattern.cpp
  sp-polygon.cpp
  sp-polyline.cpp
  sp-radial-gradient.cpp
  sp-rect.cpp
  sp-root.cpp
  sp-script.cpp
  sp-shape.cpp
  sp-solid-color.cpp
  sp-spiral.cpp
  sp-star.cpp
  sp-stop.cpp
  sp-string.cpp
  sp-style-elem.cpp
  sp-switch.cpp
  sp-symbol.cpp
  sp-tag-use-reference.cpp
  sp-tag-use.cpp
  sp-tag.cpp
  sp-text.cpp
  sp-title.cpp
  sp-tref-reference.cpp
  sp-tref.cpp
  sp-tspan.cpp
  sp-use-reference.cpp
  sp-use.cpp
  splivarot.cpp
  viewbox.cpp

  # -------
  # Headers
  attribute-rel-css.h
  attribute-rel-svg.h
  attribute-rel-util.h
  attribute-sort-util.h
  sp-anchor.h
  sp-clippath.h
  sp-conn-end-pair.h
  sp-conn-end.h
  sp-cursor.h
  sp-defs.h
  sp-desc.h
  sp-ellipse.h
  sp-factory.h
  sp-filter-primitive.h
  sp-filter-reference.h
  sp-filter-units.h
  sp-filter.h
  sp-flowdiv.h
  sp-flowregion.h
  sp-flowtext.h
  sp-font-face.h
  sp-font.h
  sp-glyph-kerning.h
  sp-glyph.h
  sp-gradient-reference.h
  sp-gradient-spread.h
  sp-gradient-units.h
  sp-gradient-vector.h
  sp-gradient.h
  sp-guide-attachment.h
  sp-guide-constraint.h
  sp-guide.h
  sp-hatch-path.h
  sp-hatch.h
  sp-image.h
  sp-item-group.h
  sp-item-notify-moveto.h
  sp-item-rm-unsatisfied-cns.h
  sp-item-transform.h
  sp-item-update-cns.h
  sp-item.h
  sp-line.h
  sp-linear-gradient.h
  sp-lpe-item.h
  sp-marker-loc.h
  sp-marker.h
  sp-mask.h
  sp-mesh-array.h
  sp-mesh-gradient.h
  sp-mesh-patch.h
  sp-mesh-row.h
  sp-metadata.h
  sp-missing-glyph.h
  sp-namedview.h
  sp-object-group.h
  sp-object.h
  sp-offset.h
  sp-paint-server-reference.h
  sp-paint-server.h
  sp-path.h
  sp-pattern.h
  sp-polygon.h
  sp-polyline.h
  sp-radial-gradient.h
  sp-rect.h
  sp-root.h
  sp-script.h
  sp-shape.h
  sp-solid-color.h
  sp-spiral.h
  sp-star.h
  sp-stop.h
  sp-string.h
  sp-style-elem.h
  sp-switch.h
  sp-symbol.h
  sp-tag.h
  sp-tag-use.h
  sp-tag-use-reference.h
  sp-text.h
  sp-textpath.h
  sp-title.h
  sp-tref-reference.h
  sp-tref.h
  sp-tspan.h
  sp-use-reference.h
  sp-use.h
  viewbox.h
)

set(inkscape_SRC
  attributes.cpp
  axis-manip.cpp
  box3d-side.cpp
  box3d.cpp
  color-profile.cpp
  color.cpp
  composite-undo-stack-observer.cpp
  conditions.cpp
  conn-avoid-ref.cpp
  console-output-undo-observer.cpp
  context-fns.cpp
  desktop-events.cpp
  desktop-style.cpp
  desktop.cpp
  device-manager.cpp
  dir-util.cpp
  document-subset.cpp
  document-undo.cpp
  document.cpp
  ege-color-prof-tracker.cpp
  event-log.cpp
  extract-uri.cpp
  file.cpp
  filter-chemistry.cpp
  filter-enums.cpp
  gc-anchored.cpp
  gc-finalized.cpp
  gradient-chemistry.cpp
  gradient-drag.cpp
  graphlayout.cpp
  guide-snapper.cpp
  help.cpp
  id-clash.cpp
  inkscape.cpp
  knot-holder-entity.cpp
  knot-ptr.cpp
  knot.cpp
  knotholder.cpp
  layer-fns.cpp
  layer-manager.cpp
  layer-model.cpp
  line-geometry.cpp
  line-snapper.cpp
  main-cmdlineact.cpp
  main-cmdlinexact.cpp
  media.cpp
  message-context.cpp
  message-stack.cpp
  mod360.cpp
  object-hierarchy.cpp
  object-set.cpp
  object-snapper.cpp
  path-chemistry.cpp
  persp3d-reference.cpp
  persp3d.cpp
  perspective-line.cpp
  preferences.cpp
  prefix.cpp
  print.cpp
  profile-manager.cpp
  proj_pt.cpp
  pure-transform.cpp
  rdf.cpp
  removeoverlap.cpp
  resource-manager.cpp
  rubberband.cpp
  satisfied-guide-cns.cpp
  selcue.cpp
  selection-chemistry.cpp
  selection-describer.cpp
  selection.cpp
  seltrans-handles.cpp
  seltrans.cpp
  shortcuts.cpp
  snap-preferences.cpp
  snap.cpp
  snapped-curve.cpp
  snapped-line.cpp
  snapped-point.cpp
  snapper.cpp
  style-internal.cpp
  style.cpp
  svg-view-widget.cpp
  svg-view.cpp
  text-chemistry.cpp
  text-editing.cpp
  transf_mat_3x4.cpp
  unclump.cpp
  unicoderange.cpp
  uri-references.cpp
  uri.cpp
  vanishing-point.cpp
  verbs.cpp
  version.cpp

  # -------
  # Headers
  MultiPrinter.h
  PylogFormatter.h
  TRPIFormatter.h
  attributes.h
  axis-manip.h
  bad-uri-exception.h
  box3d-side.h
  box3d.h
  cms-color-types.h
  cms-system.h
  color-profile-cms-fns.h
  color-profile.h
  color-rgba.h
  color.h
  colorspace.h
  composite-undo-stack-observer.h
  conditions.h
  conn-avoid-ref.h
  console-output-undo-observer.h
  context-fns.h
  decimal-round.h
  desktop-events.h
  desktop-style.h
  desktop.h
  device-manager.h
  dir-util.h
  document-private.h
  document-subset.h
  document-undo.h
  document.h
  ege-color-prof-tracker.h
  enums.h
  event-log.h
  event.h
  extract-uri.h
  file.h
  fill-or-stroke.h
  filter-chemistry.h
  filter-enums.h
  gc-anchored.h
  gc-finalized.h
  gradient-chemistry.h
  gradient-drag.h
  graphlayout.h
  guide-snapper.h
  help.h
  helper-fns.h
  icon-size.h
  id-clash.h
  inkscape-version.h
  inkscape.h
  isinf.h
  knot-enums.h
  knot-holder-entity.h
  knot-ptr.h
  knot.h
  knotholder.h
  layer-fns.h
  layer-manager.h
  layer-model.h
  line-geometry.h
  line-snapper.h
  macros.h
  main-cmdlineact.h
  main-cmdlinexact.h
  media.h
  menus-skeleton.h
  message-context.h
  message-stack.h
  message.h
  mod360.h
  number-opt-number.h
  object-hierarchy.h
  object-set.h
  object-snapper.h
  path-chemistry.h
  path-prefix.h
  persp3d-reference.h
  persp3d.h
  perspective-line.h
  preferences-skeleton.h
  preferences.h
  prefix.h
  print.h
  profile-manager.h
  proj_pt.h
  pure-transform.h
  rdf.h
  remove-last.h
  removeoverlap.h
  require-config.h
  resource-manager.h
  round.h
  rubberband.h
  satisfied-guide-cns.h
  selcue.h
  selection-chemistry.h
  selection-describer.h
  selection.h
  seltrans-handles.h
  seltrans.h
  shortcuts.h
  snap-candidate.h
  snap-enums.h
  snap-preferences.h
  snap.h
  snapped-curve.h
  snapped-line.h
  snapped-point.h
  snapper.h
  splivarot.h
  streq.h
  strneq.h
  style-enums.h
  style-internal.h
  style.h
  svg-profile.h
  svg-view-widget.h
  svg-view.h
  syseq.h
  text-chemistry.h
  text-editing.h
  text-tag-attributes.h
  transf_mat_3x4.h
  unclump.h
  undo-stack-observer.h
  unicoderange.h
  uri-references.h
  uri.h
  vanishing-point.h
  verbs.h
  version.h
)
  
# -----------------------------------------------------------------------------
# Generate version file
# -----------------------------------------------------------------------------

# a custom target that is always built
add_custom_target(
    inkscape_version ALL
    COMMAND ${CMAKE_COMMAND}
    -DINKSCAPE_SOURCE_DIR=${CMAKE_SOURCE_DIR}
    -DINKSCAPE_BINARY_DIR=${CMAKE_BINARY_DIR}
    -P ${CMAKE_SOURCE_DIR}/CMakeScripts/inkscape-version.cmake)

# buildinfo.h is a generated file
set_source_files_properties(
    ${CMAKE_BINARY_DIR}/src/inkscape-version.cpp
    PROPERTIES GENERATED TRUE)

list(APPEND inkscape_SRC
  ${CMAKE_BINARY_DIR}/src/inkscape-version.cpp
)


# -----------------------------------------------------------------------------
# Load in subdirectories
# -----------------------------------------------------------------------------

# All folders for internal inkscape
# these call add_inkscape_source
add_subdirectory(debug)
add_subdirectory(display)
add_subdirectory(extension)
add_subdirectory(filters)
add_subdirectory(helper)
add_subdirectory(io)
add_subdirectory(live_effects)
add_subdirectory(svg)
add_subdirectory(trace)
add_subdirectory(ui)
add_subdirectory(util)
add_subdirectory(widgets)
add_subdirectory(xml)
add_subdirectory(2geom)

# Directories containing lists files that describe building internal libraries
add_subdirectory(libavoid)
add_subdirectory(libcola)
add_subdirectory(libcroco)
add_subdirectory(inkgc)
add_subdirectory(libuemf)
add_subdirectory(libvpsc)
add_subdirectory(livarot)
add_subdirectory(libnrtype)
add_subdirectory(libdepixelize)

get_property(inkscape_global_SRC GLOBAL PROPERTY inkscape_global_SRC)

set(inkscape_SRC
  ${inkscape_global_SRC}
  ${inkscape_SRC}
)

# -----------------------------------------------------------------------------
# Setup the executable
# -----------------------------------------------------------------------------
set(main_SRC main.cpp)
set(view_SRC inkview.cpp)

if(WIN32)  
  # Sources for the inkscape executable on Windows.
  list(APPEND main_SRC
    registrytool.h
    registrytool.cpp
    winmain.cpp
  )
  
  # Add the platform specific resource files (enabling the app icon).
  if(${HAVE_MINGW64})
    list(APPEND main_SRC inkscape-x64.rc)
	list(APPEND view_SRC inkscape-x64.rc)
  else()
    list(APPEND main_SRC inkscape.rc)
	list(APPEND view_SRC inkscape.rc)
  endif()
  
  # Build the windows MS-DOS console executable.
  add_executable(inkscape_com winconsole.cpp)
endif()

# make executables for inkscape and inkview
add_executable(inkscape ${main_SRC})
add_executable(inkview ${view_SRC})

add_dependencies(inkscape inkscape_version)


set(INKSCAPE_TARGET_LIBS
        # order from automake
        #sp_LIB
        #nrtype_LIB
        #inkscape_LIB
        #sp_LIB # annoying, we need both!
        nrtype_LIB # annoying, we need both!
        croco_LIB
        avoid_LIB
        cola_LIB
        vpsc_LIB
        livarot_LIB
        uemf_LIB
        2geom_LIB
        depixelize_LIB
        util_LIB
        gc_LIB
        ${INKSCAPE_LIBS}
)

# Build everything except main and inkview.c in a shared library.
add_library(inkscape_base SHARED ${inkscape_SRC} ${sp_SRC})

if(WITH_DBUS)
    add_dependencies(inkscape_base inkscape_dbus)
endif()

# Link the inkscape_base library against all external dependencies
target_link_libraries(inkscape_base ${INKSCAPE_TARGET_LIBS})

# Link inkscape and inkview against inkscape_base
target_link_libraries(inkscape inkscape_base)
target_link_libraries(inkview inkscape_base)

if(NOT WIN32)
  #Define the installation
  install(TARGETS
    inkscape_base
    inkscape
    inkview 
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib/inkscape
    ARCHIVE DESTINATION lib/inkscape)
endif()
