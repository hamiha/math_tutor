import sys, os, shutil, urllib.request, hashlib
import wolframalpha
import img2pdf

server = 'http://api.wolframalpha.com/v2/query.jsp'
config = 'math_tutor.config'
app_id = ''

def main(argv):

    equations_file = argv[1]
    options = parse_config()

    print('Working.')

    print(equations_file)
    print(options)
    paths_info = solve_problems(equations_file, options)
    generate_pdf(paths_info)

    print   # pretty terminal newline

def parse_config():

    global app_id
    options = []
    file = open(config,'r')

    try:
        app_id = file.readline().split('=')[1].split('\n')[0]
    except IOError:
        print('Cannot open config file.')
    else:
        options += [app_id]

        for line in file:
            options += [line.split('=')[1].split('\n')[0]]
    finally:
        file.close()

    return options

def solve_problems(equations_file, options):

    file = open(equations_file,'r')
    client = wolframalpha.Client(app_id)
    #wolf_engine = wolf.WolframAlphaEngine(app_id, server)
    paths_info = []
    image_paths = []
    problem_num = 0

    try:
        foldername = file.readline().split('\n')[0] + '_'
    except IOError:
        print('Cannot open equations file.')
    else:
        paths_info += [foldername]

        if os.path.exists(foldername):
            shutil.rmtree(foldername, ignore_errors=True)

        try:
            os.makedirs(foldername)
        except OSError:
            print('Cannot create destination directory')
        else:
            for line in file:
                input = line
                inputs = input.split()
                print(inputs)
                query_str = inputs[2]
                #query_str = inputs[2] + '&includepodid='
                #query_str = client.query(input) + '&includepodid='
                image_num = 0
                print("1",query_str)
                '''
                if 'from' in query_str or 'derivative' in query_str:
                    query_type = 'Input'
                else:
                    query_type = 'IndefiniteIntegral'

                query_str += query_type
                print("2",query_str)
                if options[1].lower() == 'true':
                    query_str += ('&podstate=' + query_type +
                                '__Step-by-step%20solution')
                print("3",query_str)
                if options[2].lower() == 'true':
                    query_str += '&includepodid=Plot'
                #client.query(query_str)
                '''
                print("query_str",query_str)
                result = client.query(query_str)
                print("result",result)
                #result = wolf.WolframAlphaQueryResult(result)

                for pod in result.pods:
                    for subpod in pod.subpods:
                        print("subpod",subpod)
                        img = subpod.img
                        # print(img['@src'])
                        #print(list(img))
                        #src = wolframalpha.scanbranches(img[0], 'src')[0]
                        src = list(img)[0]
                        #print(src)
                        #print(src['@src'])
                        print(src['@alt'])

                        image_path = (foldername + '/' + str(problem_num) + '.' +
                                str(image_num) + '__'+ "__" + ".gif")
                        urllib.request.urlretrieve(src['@src'],image_path)
                        print(image_path)
                        #image_paths.append(image_path)
                        image_paths.append(image_path)

                        image_num += 1

                problem_num += 1

            paths_info += [image_paths]
    finally:
        file.close()

    return paths_info

def generate_pdf(paths_info):

    dir = paths_info[0]
    paths = paths_info[1]
    pdf_bytes = img2pdf.convert(paths, dpi=150, x=0, y=0)
    file = open(dir + '/' + dir + ".pdf","wb")

    try:
        file.write(pdf_bytes)
    except IOError:
        print('Cannot write PDF file.')
    finally:
        file.close()

if __name__ == "__main__":
    main(sys.argv)
