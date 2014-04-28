from openerp.osv import fields, osv

class real_estate_product(osv.osv):
    _inherit = "product.product"
    _name = "real.estate.product"
    _description = "Real Estate Product"

    _columns = {
        'real_estate' : fields.boolean('Real Estate'),
        'real_estate_type' : fields.selection((('l', 'Land'), ('f', 'Flat')), 'Type', required=True),
        'real_estate_size' : fields.float('Size', required=True),
        'real_estate_state' : fields.selection((('a', 'Available'), ('n', 'Not Available')), 'State', required=True),
        'real_estate_for_sell' : fields.boolean('For Sell'),
        'real_estate_for_rent' : fields.boolean('For Rent'),
        'real_estate_flat_type' : fields.selection((('v', 'Villa'), ('f', 'Flat'), ('d', 'Duplex')), 'Flat Type'),
        'real_estate_num_of_bed_rooms' : fields.integer('Number of bed rooms'),
        'real_estate_num_of_bath_rooms' : fields.integer('Number of bath rooms'),   
    }

    _defaults = {

        'real_estate_type' : 'l',
        'real_estate_state' : 'a',
    }

real_estate_product()    
