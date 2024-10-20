# This is a backpropagation-free Artificial Neural Network algorithm developed by Sapiens Technology®.
# The algorithm is a simplified reduction without hidden layers to an example application of a HurNet-type Neural Network.
# This version of the network works only with tabular numerical data, that is, two-dimensional numerical arrays distributed between rows and columns.
# HurNet networks are a technological creation of Sapiens Technology® and their distribution or copying without our permission is strictly prohibited.
# We do not permit copying, distribution or back-engineering of this or other versions of the HurNet network or any other code developed by Sapiens Technology®.
# We will prosecute anyone who fails to comply with the rules set out here or who discloses any details about this code.
class SingleLayerHurNet:
    def __init__(self):
        try:
            def installModule(module_name=''):
                try:
                    from subprocess import check_call, CalledProcessError
                    from sys import executable
                    module_name = str(module_name).strip()
                    check_call([executable, '-m', 'pip', 'install', module_name])
                    print(f'Module {module_name} installed successfully!')
                except CalledProcessError as error:
                    print(f'ERROR installing the module "{module_name}": {error}')
                    print('Run the command:\npip install '+module_name)
            try: from numpy import array, sum, mean, linalg, argmin
            except:
                installModule('numpy')
                try: from numpy import array, sum, mean, linalg, argmin
                except:
                    print('Run the following command and then try again:\n!pip install numpy')
                    exit()
            from pickle import dump, load
            from os import path
            self.__array = array
            self.__sum = sum
            self.__mean = mean
            self.__linalg = linalg
            self.__argmin = argmin
            self.__dump = dump
            self.__load = load
            self.__path = path
            self.__weights = None
            self.__input_layer = None
        except Exception as error: print('ERROR in class construction: '+str(error))
    def __proximityCalculation(self, input_layer):
        differences = self.__array(self.__input_layer) - input_layer
        distances = self.__linalg.norm(differences, axis=1)
        return self.__argmin(distances)
    def saveModel(self, path=''):
        try:
            if not path: filename = 'model.hur'
            else:
                filename = str(path).strip()
                if not filename.endswith('.hur'): filename += '.hur'
            data = {'input_layer': self.__input_layer, 'weights': self.__weights}
            with open(filename, 'wb') as file: self.__dump(data, file)
            return self.__path.exists(filename)
        except Exception as error:
            print('ERROR in saveModel: '+str(error))
            return False
    def loadModel(self, path=''):
        try:
            if not path: filename = 'model.hur'
            else:
                filename = str(path).strip()
                if not filename.endswith('.hur'): filename += '.hur'
            if not self.__path.exists(filename):
                print(f'The {filename} file does not exist!!')
                return False
            with open(filename, 'rb') as file:
                data = self.__load(file)
                self.__input_layer = data.get('input_layer', None)
                self.__weights = data.get('weights', None)
            return True
        except Exception as error:
            print(f'ERROR in loadModel: '+str(error))
            return False
    def train(self, input_layer=[], output_layer=[], linear=True):
        try:
            input_array = self.__array(input_layer)
            output_array = self.__array(output_layer)
            sum_inputs = self.__sum(input_array, axis=1, keepdims=True)
            sum_inputs[sum_inputs == 0] = 1
            weights_per_sample = output_array / sum_inputs
            self.__weights = self.__mean(weights_per_sample, axis=0) if not linear else weights_per_sample
            self.__input_layer = input_array
            return True
        except Exception as error:
            print(f'ERROR in train: '+str(error))
            return False
    def predict(self, input_layer=[]):
        try:
            if self.__weights is None:
                print('No training has been carried out yet!!')
                return []
            input_array = self.__array(input_layer)
            if len(self.__weights) > 0 and type(self.__weights[0]) not in (tuple, list, type(input_array)):
                sum_inputs = self.__sum(input_array, axis=1, keepdims=True)
                sum_inputs[sum_inputs == 0] = 1
                outputs = sum_inputs * self.__array(self.__weights)
                return outputs.tolist()
            else:
                outputs = []
                for inputs in input_array:
                    nearest_index = self.__proximityCalculation(input_layer=inputs)
                    weights = self.__weights[nearest_index]
                    sum_inputs = self.__sum(inputs)
                    if sum_inputs == 0: sum_inputs = 1
                    output = sum_inputs * self.__array(weights)
                    outputs.append(output.tolist())
                return outputs
        except Exception as error:
            print(f'ERROR in predict: '+str(error))
            return []
# This is a backpropagation-free Artificial Neural Network algorithm developed by Sapiens Technology®.
# The algorithm is a simplified reduction without hidden layers to an example application of a HurNet-type Neural Network.
# This version of the network works only with tabular numerical data, that is, two-dimensional numerical arrays distributed between rows and columns.
# HurNet networks are a technological creation of Sapiens Technology® and their distribution or copying without our permission is strictly prohibited.
# We do not permit copying, distribution or back-engineering of this or other versions of the HurNet network or any other code developed by Sapiens Technology®.
# We will prosecute anyone who fails to comply with the rules set out here or who discloses any details about this code.
