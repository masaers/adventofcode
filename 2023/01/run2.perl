#!/usr/bin/perl -l

    # zero 0
my %DICT = qw(
    one 1
    two 2
    three 3
    four 4
    five 5
    six 6
    seven 7
    eight 8
    nine 9
    0 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9
    );
my $KEY = join("|", keys %DICT);
my $sum = 0;
while (<>) {
    # chomp;
    # print;
    s/^.*?($KEY)/$DICT{$1}/;
    s/^(.*)($KEY).*?$/$1$DICT{$2}/;
    s/^(.)$/$1$1/;
    s/^(.?).*(.)$/$1$2/;
    my $n = int($_);
    # print $n;
    $sum += int($_);
}
print("$sum")
