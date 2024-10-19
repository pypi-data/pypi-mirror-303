: $Id: netstim.mod 2212 2008-09-08 14:32:26Z hines $
: comments at end

NEURON	{ 
    ARTIFICIAL_CELL NetStim
    THREADSAFE
    RANGE interval, number, start
    RANGE noise
    RANDOM ranvar
}

PARAMETER {
    interval    = 10 (ms) <1e-9,1e9>    : time between spikes (msec)
    number      = 10 <0,1e9>            : number of spikes (independent of noise)
    start       = 50 (ms)               : start of first spike
    noise       = 0 <0,1>               : amount of randomness (0.0 - 1.0)
}

ASSIGNED {
    event (ms)
    on
    ispike
}

INITIAL {
    seed(0)
    on = 0 : off
    ispike = 0
    if (noise < 0) {
        noise = 0
    }
    if (noise > 1) {
        noise = 1
    }
    if (start >= 0 && number > 0) {
        on = 1
        : randomize the first spike so on average it occurs at
        : start + noise*interval
        event = start + invl(interval) - interval*(1. - noise)
        : but not earlier than 0
        if (event < 0) {
            event = 0
        }
        net_send(event, 3)
    }
}	

PROCEDURE init_sequence(t(ms)) {
    if (number > 0) {
        on = 1
        event = 0
        ispike = 0
    }
}

FUNCTION invl(mean (ms)) (ms) {
    if (mean <= 0.) {
        mean = .01 (ms) : I would worry if it were 0.
    }
    if (noise == 0) {
        invl = mean
    } else {
        invl = (1. - noise)*mean + noise*mean*erand()
    }
}

FUNCTION erand() {
    erand = random_negexp(ranvar)
}

PROCEDURE next_invl() {
    if (number > 0) {
        event = invl(interval)
    }
    if (ispike >= number) {
        on = 0
    }
}

NET_RECEIVE (w) {
    if (flag == 0) { : external event
        if (w > 0 && on == 0) { : turn on spike sequence
            : but not if a netsend is on the queue
            init_sequence(t)
            : randomize the first spike so on average it occurs at
            : noise*interval (most likely interval is always 0)
            next_invl()
            event = event - interval*(1. - noise)
            net_send(event, 1)
        }else if (w < 0) { : turn off spiking definitively
            on = 0
        }
    }
    if (flag == 3) { : from INITIAL
        if (on == 1) { : but ignore if turned off by external event
            init_sequence(t)
            net_send(0, 1)
        }
    }
    if (flag == 1 && on == 1) {
        ispike = ispike + 1
        net_event(t)
        next_invl()
        if (on == 1) {
            net_send(event, 1)
        }
    }
}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
: Legacy API
:
:    Difference: seed(x) merely sets ranvar sequence to ((uint32_t)x, 0)
:                noiseFromRandom HOC Random object must use Random123
:                    generator. The ids and sequence are merely copied
:                    into ranvar.
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

: the Random idiom has been extended to support CoreNEURON.

: For backward compatibility, noiseFromRandom(hocRandom) can still be used
: as well as the default low-quality scop_exprand generator.
: However, CoreNEURON will not accept usage of the low-quality generator,
: and, if noiseFromRandom is used to specify the random stream, that stream
: must be using the Random123 generator.

: The recommended idiom for specfication of the random stream is to use
: noiseFromRandom123(id1, id2[, id3])

: If any instance uses noiseFromRandom123, then no instance can use noiseFromRandom
: and vice versa.


COMMENT
Presynaptic spike generator
---------------------------

This mechanism has been written to be able to use synapses in a single
neuron receiving various types of presynaptic trains.  This is a "fake"
presynaptic compartment containing a spike generator.  The trains
of spikes can be either periodic or noisy (Poisson-distributed)

Parameters;
   noise: 	between 0 (no noise-periodic) and 1 (fully noisy)
   interval: 	mean time between spikes (ms)
   number: 	number of spikes (independent of noise)

Written by Z. Mainen, modified by A. Destexhe, The Salk Institute

Modified by Michael Hines for use with CVode
The intrinsic bursting parameters have been removed since
generators can stimulate other generators to create complicated bursting
patterns with independent statistics (see below)

Modified by Michael Hines to use logical event style with NET_RECEIVE
This stimulator can also be triggered by an input event.
If the stimulator is in the on==0 state (no net_send events on queue)
 and receives a positive weight
event, then the stimulator changes to the on=1 state and goes through
its entire spike sequence before changing to the on=0 state. During
that time it ignores any positive weight events. If, in an on!=0 state,
the stimulator receives a negative weight event, the stimulator will
change to the on==0 state. In the on==0 state, it will ignore any ariving
net_send events. A change to the on==1 state immediately fires the first spike of
its sequence.

ENDCOMMENT

PROCEDURE seed(x) {
    random_setseq(ranvar, x)
}

PROCEDURE noiseFromRandom() {
VERBATIM
#if !NRNBBCORE
 {
    if (ifarg(1)) {
        Rand* r = nrn_random_arg(1);
        uint32_t id[3];
        if (!nrn_random_isran123(r, &id[0], &id[1], &id[2])) {
            hoc_execerr_ext("NetStim: Random.Random123 generator is required.");
        }
        nrnran123_setids(ranvar, id[0], id[1], id[2]);
        char which;
        nrn_random123_getseq(r, &id[0], &which);
        nrnran123_setseq(ranvar, id[0], which);
    }
 }
#endif
ENDVERBATIM
}

PROCEDURE noiseFromRandom123() {
VERBATIM
#if !NRNBBCORE
    if (ifarg(3)) {
        nrnran123_setids(ranvar, static_cast<uint32_t>(*getarg(1)), static_cast<uint32_t>(*getarg(2)), static_cast<uint32_t>(*getarg(3)));
    } else if (ifarg(2)) {
        nrnran123_setids(ranvar, static_cast<uint32_t>(*getarg(1)), static_cast<uint32_t>(*getarg(2)), 0);
    }
    nrnran123_setseq(ranvar, 0, 0);
#endif
ENDVERBATIM
}
