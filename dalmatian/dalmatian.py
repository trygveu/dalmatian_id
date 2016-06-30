import puppy
import argparse
import os
import errno


def main():
    parser = argparse.ArgumentParser(description="Dalmation ID Problem"
                                     "Generates the puppy population")
    names = open('./resources/dognames.txt', 'r')
    path = './population/'
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
    dalmatians = [puppy.Puppy() for i in range(101)]
    for i, p in enumerate(dalmatians):
        p.name = names.readline().strip()
        filename = '{0}{1:03d}-{2}.svg'.format(path, i + 1, p.name)
        p.write_svg(filename)
        print('Writing {}'.format(filename))

if __name__ == '__main__':
    main()
