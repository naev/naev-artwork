RES := $(if $(HIDPI),800x800,400x400)
OUTDIR := ../out/exterior
PNG_OUTPUTS := $(patsubst %.png,$(OUTDIR)/%.png,$(wildcard *.png))
JPG_OUTPUTS := $(patsubst %.jpg,$(OUTDIR)/%.png,$(wildcard *.jpg))
OUTPUTS := $(PNG_OUTPUTS) $(JPG_OUTPUTS)

all: $(OUTPUTS)

$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%.png: %.jpg | $(OUTDIR)
	convert -scale $(RES) "$<" "$@"

$(OUTDIR)/%.png: %.png | $(OUTDIR)
	convert -scale $(RES) "$<" "$@"

clean:
	rm -f out/*

.PHONY:
	all clean
