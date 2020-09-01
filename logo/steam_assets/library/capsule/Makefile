OUTDIR := ../../../out/steam
OUTPUTS := $(patsubst %.mlt,$(OUTDIR)/%.png,$(wildcard *.mlt))

all: $(OUTPUTS)
$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%.png: %.mlt | $(OUTDIR)
	./render_library_capsule.sh -f "$<" -o "$(OUTDIR)"

.PHONY: all
