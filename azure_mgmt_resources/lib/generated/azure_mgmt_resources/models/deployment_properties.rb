# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Resources
  module Models
    #
    # Deployment properties.
    #
    class DeploymentProperties

      include MsRestAzure

      # @return Gets or sets the template content. Use only one of Template or
      # TemplateLink.
      attr_accessor :template

      # @return [TemplateLink] Gets or sets the URI referencing the template.
      # Use only one of Template or TemplateLink.
      attr_accessor :template_link

      # @return Deployment parameters. Use only one of Parameters or
      # ParametersLink.
      attr_accessor :parameters

      # @return [ParametersLink] Gets or sets the URI referencing the
      # parameters. Use only one of Parameters or ParametersLink.
      attr_accessor :parameters_link

      # @return [DeploymentMode] Gets or sets the deployment mode. Possible
      # values include: 'Incremental', 'Complete'
      attr_accessor :mode

      # @return [DebugSetting] Gets or sets the debug setting of the
      # deployment.
      attr_accessor :debug_setting


      #
      # Mapper for DeploymentProperties class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'DeploymentProperties',
          type: {
            name: 'Composite',
            class_name: 'DeploymentProperties',
            model_properties: {
              template: {
                required: false,
                serialized_name: 'template',
                type: {
                  name: 'Object'
                }
              },
              template_link: {
                required: false,
                serialized_name: 'templateLink',
                type: {
                  name: 'Composite',
                  class_name: 'TemplateLink'
                }
              },
              parameters: {
                required: false,
                serialized_name: 'parameters',
                type: {
                  name: 'Object'
                }
              },
              parameters_link: {
                required: false,
                serialized_name: 'parametersLink',
                type: {
                  name: 'Composite',
                  class_name: 'ParametersLink'
                }
              },
              mode: {
                required: true,
                serialized_name: 'mode',
                type: {
                  name: 'Enum',
                  module: 'DeploymentMode'
                }
              },
              debug_setting: {
                required: false,
                serialized_name: 'debugSetting',
                type: {
                  name: 'Composite',
                  class_name: 'DebugSetting'
                }
              }
            }
          }
        }
      end
    end
  end
end