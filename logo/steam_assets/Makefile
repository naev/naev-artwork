OUTDIR := ../out/logo

all: store soundtrack library

store:
	mkdir -p $(OUTDIR)
	$(MAKE) -C store

soundtrack:
	mkdir -p $(OUTDIR)
	$(MAKE) -C soundtrack

library:
	mkdir -p $(OUTDIR)
	$(MAKE) -C library

.PHONY: store soundtrack library
